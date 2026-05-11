# Lab 5: A Tip Calculator Toolkit with Functions

## Objective

In this lab, you'll practice writing functions to build a small, reusable **tip calculator** around a list of subtotals (for example, separate cheques at a table). You will split the work into clear functions and a short main-style flow.

## Scenario: Tip calculator with functions

You are turning informal arithmetic into a tidy toolkit:

- Start from a list of subtotal amounts (floats)
- Write a function that returns the tip in pounds/dollars for one subtotal and a tip percentage
- Write a function that filters subtotals above a threshold (for example, “flag large bills”)
- Write a function that summarises the whole list at a chosen tip rate

---

## Task 1: Getting Started

**Your task:** Set up your workspace and the sample data.

**What to do:**

1. Create a new Python file called `tip_calculator.py`
2. Copy the list of subtotals below into your file
3. Run the file once to confirm there are no syntax errors

**Sample data (copy into your file):**

```python
check_amounts = [
    45.00,
    32.50,
    78.20,
    19.99,
    54.00,
    120.00,
    28.75,
    63.40,
    15.00,
    41.10,
]
```

**Expected outcome:**

- You have a Python file containing the list
- The file runs (even if it prints nothing yet)

**Check your work:**

- Does the list contain ten amounts?
- Are the values numeric types suitable for money at this stage of the course (typically `float`)?

<details>
<summary>Possible Solution for Task 1</summary>

```python
# tip_calculator.py
# Paste `check_amounts` here so the functions below can use it.
```

</details>

---

## Task 2: Tip for one subtotal

**Your task:** Write a function that returns the tip amount for a single bill.

**What to do:**

1. Define a function called `tip_amount(subtotal, tip_percent)`
2. `subtotal` is the bill before tip; `tip_percent` is a whole number such as `18` meaning eighteen percent (not `0.18`)
3. Return the tip in currency units (same unit as the subtotal)

**Hints:**

- Start with `def tip_amount(subtotal, tip_percent):`
- Convert the percentage to a multiplier you can apply to `subtotal`
- Use `return` so other functions can reuse the result

**Expected outcome:**

- Calling the function with known values matches a hand calculation
- The function does not print; it returns a number

**Check your work:**

- Does `tip_amount(100.0, 18)` return `18.0`?
- Does the definition use `def` and `return` correctly?

<details>
<summary>Possible Solution for Task 2</summary>

```python
def tip_amount(subtotal, tip_percent):
    return subtotal * (tip_percent / 100)
```

</details>

---

## Task 3: Subtotals above a threshold

**Your task:** Write a function that filters the list of subtotals.

**What to do:**

1. Define `amounts_above(amounts, threshold)`
2. Parameters: a list of numbers and a single threshold value
3. Return a **new list** containing only the amounts strictly greater than `threshold` (useful for spotting “large” bills in a batch)

**Hints:**

- Initialise an empty list, loop, and append when the condition passes
- Alternatively, plan ahead for the next lab and sketch how a comprehension might look later—here, a plain loop is perfect

**Expected outcome:**

- Given the sample data, `amounts_above(check_amounts, 50.0)` should include `78.20`, `54.00`, `120.00`, and `63.40`, and exclude smaller amounts
- The original `check_amounts` list should remain unchanged

**Check your work:**

- Does the function return a list of floats?
- Do values exactly equal to the threshold follow the rule you chose? (Document your choice: strict `>` vs `>=`.)

<details>
<summary>Possible Solution for Task 3</summary>

```python
def amounts_above(amounts, threshold):
    out = []
    for amount in amounts:
        if amount > threshold:
            out.append(amount)
    return out
```

</details>

---

## Task 4: Summarise every cheque at one tip rate

**Your task:** Write a function that analyses the full list using `tip_amount`.

**What to do:**

1. Define `summarise_checks(amounts, tip_percent)`
2. For each subtotal, compute tip and total (subtotal + tip)
3. Print a short summary: how many cheques, average subtotal, average tip, and average total with tip—use your `tip_amount` helper inside the loop

**Hints:**

- Accumulate totals in running sums, then divide by `len(amounts)` when computing averages
- Guard against an empty list if you want to be extra safe (optional extension)

**Expected outcome:**

- Clear printed lines suitable for a quick sanity check in a restaurant back-office script
- Confirms you can call one function from inside another

**Check your work:**

- Are averages computed with the correct divisor?
- Does every subtotal flow through `tip_amount`?

<details>
<summary>Possible Solution for Task 4</summary>

```python
def summarise_checks(amounts, tip_percent):
    n = len(amounts)
    sum_sub = 0.0
    sum_tip = 0.0
    sum_total = 0.0
    for sub in amounts:
        tip = tip_amount(sub, tip_percent)
        sum_sub += sub
        sum_tip += tip
        sum_total += sub + tip
    print(f"Cheques: {n}")
    print(f"Average subtotal: {sum_sub / n:.2f}")
    print(f"Average tip: {sum_tip / n:.2f}")
    print(f"Average total (with tip): {sum_total / n:.2f}")
```

</details>

---

## Tying It All Together

**Your task:** Call your functions from the bottom of the script.

**What to do:**

1. After defining the functions, call `summarise_checks` with `check_amounts` and a tip rate you choose (for example `18`)
2. Call `amounts_above` with a threshold you pick and print the returned list or its length
3. Read the output like a sceptical accountant—do the numbers feel plausible?

**Hints:**

- Try more than one threshold or tip percent while experimenting
- Keep printed labels aligned with what each number represents

**Expected outcome:**

- A runnable script demonstrating all three behaviours
- Output you could show to someone else without extra explanation

---

## Example Interaction

```
Cheques: 10
Average subtotal: 49.79
Average tip: 8.96
Average total (with tip): 58.75
Amounts above 50.0: [78.2, 54.0, 120.0, 63.4]
```

(Exact formatting may differ; focus on correctness first.)

---

**You're done when** your program defines the three functions, uses `tip_amount` inside `summarise_checks`, and demonstrates `amounts_above` on the sample data.

---

## Key Concepts Demonstrated

- Defining functions with `def`
- Parameters, arguments, and return values
- Reusing helpers inside higher-level functions
- Light-weight “data” thinking: batches of numbers in a list

---

## Check your work

Before moving on, reflect briefly:

### Basic Concepts:

- [ ] What problem does splitting code into functions solve for you as the author?
- [ ] When should a function print versus return?
- [ ] How do parameters get their values when you call a function?

### Practical Skills:

- [ ] Can you write a numeric helper and test it with simple inputs?
- [ ] Can you filter a list into a new list without mutating the original?
- [ ] Can you combine loops and arithmetic to produce averages?

### If any answer felt shaky:

- Re-read Tasks 2–4
- Sketch the values on paper for one loop iteration

---

## Common Issues

### Problem: "NameError: name 'tip_amount' is not defined"

**Fix:** Define `tip_amount` above any function that calls it.

### Problem: Tips are wildly large or tiny

**Fix:** Confirm whether `tip_percent` is meant to be `18` or `0.18` and stay consistent with the lab contract.

### Problem: `amounts_above` returns an empty list unexpectedly

**Fix:** Check whether you used `>` or `>=` and whether the threshold matches the data scale you expect.

---

## Extension Ideas (Optional)

1. Add `total_with_tip(subtotal, tip_percent)` that returns subtotal plus tip without printing.
2. Return summary statistics as a dictionary instead of printing them.
3. Round displayed currency to two decimal places everywhere for tidier output.

---

## Next Steps

In the next lab, you'll express similar “map and filter” ideas with **list comprehensions**, using **ticket codes** as the dataset.

Move on to Lab 6: List Comprehensions!

---

## Solutions

**Complete code examples for all exercises are available in the `solutions/lab-05` folder.**

- `solutions/tip_calculator.py` — reference implementation
- `solutions/step_by_step/` — individual step solutions

**Try to solve the exercises yourself first, then check the solutions if you get stuck!**

---

## Questions?

If you get stuck or have questions:

1. Read error messages carefully
2. Review the concepts in the notes
3. Look at the solutions folder for examples
4. Ask for help from your instructor or classmates
5. Remember: everyone learns at their own pace!
