"""
Small maths library used in the testing lab.

Design rule:
- Only `int` and `float` are accepted.
- `bool` is rejected (even though it's a subclass of `int`).
- Invalid input types raise `TypeError`.
"""


def _validate_numbers(a, b):
    """Validate that a and b are numbers, rejecting bool."""
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("Both arguments should be numbers.")

    # bool is a subclass of int, so we must explicitly reject it.
    if isinstance(a, bool) or isinstance(b, bool):
        raise TypeError("Both arguments should be numbers.")


def add(a, b):
    _validate_numbers(a, b)
    # Round to keep float arithmetic stable for simple teaching examples.
    return round(a + b, 8)


def subtract(a, b):
    _validate_numbers(a, b)
    return round(a - b, 8)


def multiply(a, b):
    _validate_numbers(a, b)
    return round(a * b, 8)


def divide(a, b):
    _validate_numbers(a, b)
    # Allow Python's normal division-by-zero behavior.
    return round(a / b, 8)