# Lab 10: Testing a Small Class with pytest

## Objective

In this lab, you'll write a few automated tests for the `Ticket` class using `pytest`.

You are **not** changing the `Ticket` implementation — only writing tests.

## Scenario: Locking in behaviour with pytest

You have a `Ticket` class that should behave consistently (store `code` / `venue`, print sensibly, count hyphen segments). Tests document those expectations so future edits do not silently break them.

---

## Task 1: Create your test file

**Your task:**

- Create a new file called `test_ticket.py`
- Place it next to `ticket_module.py`
- Import the `Ticket` class

**Check**

- Running `pytest` should discover the file (even before tests exist)

<details>
<summary>Possible Solution for Task 1</summary>

```python
# test_ticket.py
from ticket_module import Ticket

# or
class Ticket:
    def __init__(self, code, venue):
        self.code = code
        self.venue = venue

    def __str__(self):
        return f"{self.code} @ {self.venue}"

    def get_segment_count(self):
        return len(self.code.split("-"))
```

</details>

---

## Task 2: Test object creation

**Your task:**

- Write a test that:
  - creates a `Ticket`
  - asserts the code is stored correctly
  - asserts the venue is stored correctly

**Hints**

- Test function names must start with `test_`
- Use plain `assert` statements
- Keep strings short and obvious

**Check**

- The test fails if you deliberately change an expected value
- The test passes when the implementation matches

<details>
<summary>Possible Solution for Task 2</summary>

```python
def test_ticket_object_creation():
    t = Ticket("VIP-001", "Royal Albert Hall")
    assert t.code == "VIP-001"
    assert t.venue == "Royal Albert Hall"
```

</details>

---

## Task 3: Test `get_segment_count`

**Your task:**

- Write a test for `get_segment_count`
- Choose a code where counting hyphen segments is obvious
- Assert the returned integer

**Hints**

- Avoid overcomplicating punctuation on the first pass
- One clear case is enough for this task

**Check**

- If you change the code string, the expected count should change too

<details>
<summary>Possible Solution for Task 3</summary>

```python
def test_get_segment_count():
    t = Ticket("A-B-C", "Test Venue")
    assert t.get_segment_count() == 3
```

</details>

---

## Task 4: Add one edge case

Pick **one** edge case and write a test for it.

Examples (choose one):

- empty code string  
- code with no hyphens (single segment)  
- repeated hyphens creating empty segments (decide what you expect, then assert it)

**Your task:**

- Decide what _should_ happen
- Encode that decision in a test

**Check**

- The test communicates a deliberate policy, not an accident

<details>
<summary>Possible Solution for Task 4</summary>

```python
def test_get_segment_count_empty_code():
    t = Ticket("", "Unknown venue")
    assert t.get_segment_count() == 1  # "".split("-") -> ['']
```

</details>

---

## Task 5: Reduce duplication (choose one)

Pick **one** tidy-up.

### Option A: helper factory

- Write a small helper that returns a `Ticket`
- Use it in at least two tests

### Option B: parametrised test

- Use `@pytest.mark.parametrize`
- Cover multiple segment-count cases in one function

### Option C: stop

- If your tests are already crystal clear, leave them as-is

<details>
<summary>Possible Solution for Task 5</summary>

```python
# Option A sketch
def make_ticket(code: str) -> Ticket:
    return Ticket(code, "Test Venue")
```

</details>

---

## Example interaction

```
pytest
==================== 3 passed in 0.01s ====================
```

---

**You're done when** `pytest` discovers `test_ticket.py`, your tests pass, and at least one edge case is documented.

---

## Key Concepts Demonstrated

- Tests as small Python functions  
- Assertions as executable specifications  
- pytest discovery rules (`test_` prefix)  

---

## Check your work

### Running your tests

```bash
pytest
```

Optional verbosity:

```bash
pytest -v
```

---

## What matters

- Tests are ordinary Python  
- `assert` expresses intent  
- One test should emphasise one behaviour  
- Readable failures beat clever cleverness  

---

## Common Issues

- pytest cannot find your file: confirm the filename starts with `test_`  
- Assertions never run: check that your functions are named `test_...`  
- Changing expected literals without updating tests: keep expectations aligned with the rules you want  

---

## Extension ideas (optional)

1. Add a test for `__str__` / `str(ticket)`  
2. Add another `get_segment_count` edge case  
3. Parametrise several hyphen patterns in one test  

---

## Next steps

Lab 11 loads ticket rows from **`events.csv`** instead of hard-coded lists.
