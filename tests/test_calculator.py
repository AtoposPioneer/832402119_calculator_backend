import unittest

from app.calculator import CalculatorError, calculate_expression


class CalculatorTestCase(unittest.TestCase):
    def test_basic_operations(self):
        self.assertEqual(calculate_expression("1 + 2"), "3")
        self.assertEqual(calculate_expression("5 - 3"), "2")
        self.assertEqual(calculate_expression("4 * 6"), "24")
        self.assertEqual(calculate_expression("8 / 2"), "4")

    def test_compound_expressions(self):
        self.assertEqual(calculate_expression("(1 + 2) * 3"), "9")
        self.assertEqual(calculate_expression("1 + 2 * 3"), "7")
        self.assertEqual(calculate_expression("-5 + 8"), "3")
        self.assertEqual(calculate_expression("3 * -2"), "-6")
        self.assertEqual(calculate_expression("3.5 + 2.1"), "5.6")

    def test_chinese_math_symbols(self):
        self.assertEqual(calculate_expression("2 × 3"), "6")
        self.assertEqual(calculate_expression("8 ÷ 2"), "4")

    def test_invalid_expression(self):
        with self.assertRaises(CalculatorError):
            calculate_expression("1 + * 2")

    def test_division_by_zero(self):
        with self.assertRaises(CalculatorError):
            calculate_expression("1 / 0")

    def test_unsafe_expression(self):
        with self.assertRaises(CalculatorError):
            calculate_expression("__import__('os').system('echo unsafe')")


if __name__ == "__main__":
    unittest.main()
