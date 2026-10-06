# Frontend Code Style

This project mainly follows the ideas of the [Google HTML/CSS Style Guide](https://google.github.io/styleguide/htmlcssguide.html) and common JavaScript readability practices.

## HTML

- Use semantic elements where possible.
- Keep the structure readable and grouped by function.
- Use accessible labels for interactive controls.
- Keep visible text concise and directly related to user actions.

## CSS

- Use CSS variables for shared colors, spacing, and shadows.
- Keep class names meaningful and consistent.
- Use responsive layout rules for different screen sizes.
- Avoid unnecessary decorative complexity.
- Avoid deeply nested selectors.
- Keep component dimensions stable to prevent layout shifting.

## JavaScript

- Use `const` and `let` instead of `var`.
- Keep functions focused on one task.
- Use clear names for DOM elements and event handlers.
- Handle API errors with user-friendly messages.
- Keep backend URLs in a single configuration constant.
- Use `async` and `await` for API requests.
- Avoid duplicating DOM update logic.

## Frontend Responsibility

The frontend must not perform the core expression calculation. It only collects user input, sends it to the backend, and displays the backend response.

## Accessibility

- Use labels for input fields.
- Use `aria-label` or `title` for icon-only buttons.
- Keep color contrast readable in both light and dark themes.
