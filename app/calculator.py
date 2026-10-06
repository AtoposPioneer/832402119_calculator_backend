"""Safe arithmetic expression evaluation."""

from __future__ import annotations

import ast
import operator
from decimal import Decimal, DivisionByZero, InvalidOperation, getcontext


getcontext().prec = 28

MAX_EXPRESSION_LENGTH = 200

ALLOWED_BINARY_OPERATORS = {
    ast.Add: operator.add,
    ast.Sub: operator.sub,
    ast.Mult: operator.mul,
    ast.Div: operator.truediv,
}

ALLOWED_UNARY_OPERATORS = {
    ast.UAdd: operator.pos,
    ast.USub: operator.neg,
}


class CalculatorError(ValueError):
    """Raised when an expression cannot be safely calculated."""


def calculate_expression(expression: str) -> str:
    """Calculate an arithmetic expression and return a display-ready result."""

    normalized = _normalize_expression(expression)

    try:
        tree = ast.parse(normalized, mode="eval")
        result = _evaluate_node(tree.body)
    except (SyntaxError, TypeError) as exc:
        raise CalculatorError("Invalid expression.") from exc
    except (DivisionByZero, ZeroDivisionError, InvalidOperation) as exc:
        raise CalculatorError("Division by zero is not allowed.") from exc

    return _format_decimal(result)


def _normalize_expression(expression: str) -> str:
    if expression is None:
        raise CalculatorError("Expression is required.")

    normalized = expression.strip().replace("×", "*").replace("÷", "/")

    if not normalized:
        raise CalculatorError("Expression cannot be empty.")

    if len(normalized) > MAX_EXPRESSION_LENGTH:
        raise CalculatorError("Expression is too long.")

    return normalized


def _evaluate_node(node: ast.AST) -> Decimal:
    if isinstance(node, ast.BinOp):
        operator_type = type(node.op)
        if operator_type not in ALLOWED_BINARY_OPERATORS:
            raise CalculatorError("Unsupported operator.")

        left = _evaluate_node(node.left)
        right = _evaluate_node(node.right)

        if operator_type is ast.Div and right == 0:
            raise CalculatorError("Division by zero is not allowed.")

        return ALLOWED_BINARY_OPERATORS[operator_type](left, right)

    if isinstance(node, ast.UnaryOp):
        operator_type = type(node.op)
        if operator_type not in ALLOWED_UNARY_OPERATORS:
            raise CalculatorError("Unsupported unary operator.")

        operand = _evaluate_node(node.operand)
        return ALLOWED_UNARY_OPERATORS[operator_type](operand)

    if isinstance(node, ast.Constant) and isinstance(node.value, (int, float)):
        return Decimal(str(node.value))

    raise CalculatorError("Invalid expression.")


def _format_decimal(value: Decimal) -> str:
    if value == value.to_integral():
        return str(value.quantize(Decimal("1")))

    normalized = value.normalize()
    return format(normalized, "f")
