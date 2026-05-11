# Lab 10 (Alternate): Testing `divide()` and `subtract()` with pytest

## Objective

In this lab, you will step through testing `divide()` first, then `subtract()`, and practise thinking about test types before writing code.

---

## Starting Point
You should already have:
- `maths.py` with at least `add()`, `divide()`, and `subtract()`
- a pytest file (`test_maths.py` or `maths_test.py`)
- `import pytest` in your test file

---

## Test Design Thinking (before coding)
For each function, ask:
1. What is the **happy path**?
2. What are useful **edge cases**?
3. What should happen for **invalid input types**?

Keep this pattern:
- one test = one behavior
- clear test names that describe expected behavior

---

## Task 1: Test `divide()` first

### 1A. Happy-path test
Write one test where division should work normally.

**Hints**
- Choose easy numbers where the answer is obvious.
- If you use decimals, prefer `pytest.approx(...)`.

<details>
<summary>Possible Solution for 3A</summary>

```python
def test_divide_two_whole_numbers():
    result = divide(10, 2)
    assert result == 5
```

</details>

### 1B. Decide and test divide-by-zero behavior
Decide what your library should do when dividing by zero, then test that decision.

**Hint**
- If your function relies on normal Python division, this is usually `ZeroDivisionError`.

<details>
<summary>Possible Solution for 3B</summary>

```python
def test_divide_by_zero_raises():
    with pytest.raises(ZeroDivisionError):
        divide(10, 0)
```

</details>

### 1C. Test invalid types for `divide()`
Pick one or two non-number examples and assert the expected exception.

**Ideas**
- `"10"` and `2`
- `None` and `1`
- `True` and `5`

<details>
<summary>Possible Solution for 3C</summary>

```python
def test_divide_rejects_non_numbers():
    with pytest.raises(TypeError):
        divide("10", 2)
```

</details>

---

## Task 2: Test `subtract()`

### 2A. Happy-path test
Write one straightforward test for `subtract()`.

<details>
<summary>Possible Solution for 4A</summary>

```python
def test_subtract_two_whole_numbers():
    assert subtract(10, 3) == 7
```

</details>

### 2B. Edge-case test
Choose one edge case:
- negative values
- decimal values
- subtracting zero

If you choose decimals, use `pytest.approx(...)`.

<details>
<summary>Possible Solution for 4B</summary>

```python
def test_subtract_with_negative_result():
    assert subtract(3, 10) == -7
```

</details>

### 2C. Invalid-type test for `subtract()`
Add a test to confirm non-number values are rejected.

<details>
<summary>Possible Solution for 4C</summary>

```python
def test_subtract_rejects_non_numbers():
    with pytest.raises(TypeError):
        subtract([], 3)
```

</details>

---

## Task 3: Reduce duplication (optional)
If your invalid-type tests are repetitive, pick one of these refactors.

### Option A: Parametrize invalid inputs
Use one test with multiple bad input pairs.

<details>
<summary>Possible Solution for Task 3 Option A</summary>

```python
@pytest.mark.parametrize("a, b", [
    ("10", 2),
    (None, 1),
    (True, 4),
])
def test_divide_rejects_invalid_types(a, b):
    with pytest.raises(TypeError):
        divide(a, b)
```

</details>

### Option B: Add a shared validation helper and test it
If `add()`, `subtract()`, and `divide()` all repeat the same type checks, extract a helper in `maths.py` (for example `_validate_numbers(a, b)`), then test that helper directly.

**Why this helps**
- one place to maintain the type-rule
- clearer arithmetic functions
- faster feedback when type-validation behavior changes

<details>
<summary>Possible Solution for Task 3 Option B</summary>

```python
def test_validate_numbers_accepts_valid_numbers():
    # no exception means pass
    _validate_numbers(10, 2.5)

@pytest.mark.parametrize("a, b", [
    ("10", 2),
    (None, 1),
    (True, 4),
])
def test_validate_numbers_rejects_invalid_types(a, b):
    with pytest.raises(TypeError):
        _validate_numbers(a, b)
```

</details>

---

## Check Your Work
Run:

```bash
pytest
```

You are done when:
- your new `divide()` tests pass
- your new `subtract()` tests pass
- you have at least one happy-path and one error/edge test for each function

---

## Common Issues
- `pytest` discovers no tests: check file name and `test_...` function names.
- Decimal assertions fail unexpectedly: use `pytest.approx(...)`.
- Wrong exception type: confirm whether your function raises `TypeError` or something else.

