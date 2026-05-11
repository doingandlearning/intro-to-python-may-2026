# Lab 7 (Alternative): Structuring Experimental Results with Classes

## Objective

In this lab, you'll apply classes to an experimental-data domain. You will use a `ResultValue` class (detector name, date, list of numeric results), create multiple objects, and produce a short analysis report.

You will:
1. Build a `ResultValue` class from scratch
2. Add methods for average, maximum, and range
3. Create multiple objects (different detectors or dates) and store them in a list
4. Loop over that list to print a summary report
5. Add at least one extra analysis method relevant to your experiment
6. (Optional) Add/improve `__str__` to make report output cleaner

---

## Scenario: Detector Result Report

You have repeated measurements from one or more detectors across one or more dates. Instead of juggling separate lists and variables, you’ll represent each detector/date run as an object and let methods compute the stats for you.

---

## Task 1: Define the `ResultValue` Class from Scratch

Create a file `result_analysis.py` (or similar).

**Your task:**

- Define a class called `ResultValue`
- Add `__init__(self, detector_name, date)` and store:
  - `self.detector_name`
  - `self.date`
  - `self.results` (start as an empty list)
- Add a method `add_result(self, value)` that appends values into `self.results`

**Hints:**

- Start with `class ResultValue:`
- Keep all methods indented under the class
- Use `self.results.append(value)` inside `add_result(...)`

### Check your work

- Can you create `ResultValue("Detector A", "2026-03-03")`?
- Does `self.results` start empty?
- After calling `add_result(...)`, does the list grow?

<details>
<summary>Possible Solution for Task 1</summary>

```python
class ResultValue:
    def __init__(self, detector_name, date):
        self.detector_name = detector_name
        self.date = date
        self.results = []

    def add_result(self, value):
        self.results.append(value)
```

</details>

---

## Task 2: Add Core Analysis Methods

Now add methods to compute average, maximum, and range.

**Your task:**

- Add `get_average_of_results(self)`
- Add `get_maximum_of_results(self)`
- Add `get_range_of_results(self)`
- Handle empty result lists gracefully (for example, return `None`)

**Hints:**

- For average: total / count
- For max/range: use `max(...)` and `min(...)` once data exists
- Add an empty-list guard at the top of each method

### Check your work

- Do methods return numbers when results exist?
- Do they return `None` (or your chosen behavior) when no results exist?
- Can you call all three methods without errors?

<details>
<summary>Possible Solution for Task 2</summary>

```python
def get_average_of_results(self):
    if not self.results:
        return None
    return sum(self.results) / len(self.results)

def get_maximum_of_results(self):
    if not self.results:
        return None
    return max(self.results)

def get_range_of_results(self):
    if not self.results:
        return None
    return max(self.results) - min(self.results)
```

</details>

---

## Task 3: Create One Object and Compute Stats

**Your task:**

- Create one `ResultValue` object (for example detector `"Detector A"` on date `"2026-03-03"`)
- Add several numeric results using `add_result(...)`
- Print average, maximum, and range

**Hints:**

- Add at least 3 values so stats are meaningful
- Use one variable per computed value before printing

### Check your work

- Does the object store detector name, date, and a list of results?
- Do average, max, and range print as expected?
- What happens if you create an object and print stats before adding results?

<details>
<summary>Possible Solution for Task 3</summary>

```python
r = ResultValue("Detector A", "2026-03-03")
r.add_result(123)
r.add_result(141)
r.add_result(98)

avg = r.get_average_of_results()
mx = r.get_maximum_of_results()
rng = r.get_range_of_results()

print("Average:", avg)
print("Max:", mx)
print("Range:", rng)
```

</details>

---

## Task 4: Create Multiple Objects

Now model multiple runs.

**Your task:**

- Create at least 2-3 `ResultValue` objects (different detector names and/or dates)
- Add different results to each object
- Store all objects in a list such as `results_list`

**Hints:**

- Build each object fully (name/date/results), then append to the list
- Use realistic values if you have them, otherwise use simple test numbers

### Check your work

- Do you have multiple objects in one list?
- Are results different across objects?
- Can you loop over the list and print each object’s detector name/date?

<details>
<summary>Possible Solution for Task 4</summary>

```python
r1 = ResultValue("Detector A", "2026-03-03")
r1.add_result(123)
r1.add_result(141)
r1.add_result(98)

r2 = ResultValue("Detector B", "2026-03-03")
r2.add_result(210)
r2.add_result(199)
r2.add_result(205)

results_list = []
results_list.append(r1)
results_list.append(r2)
```

</details>

---

## Task 5: Print an Analysis Report

Loop over the list and print one summary line per object.

**Your task:**

- Loop over `results_list`
- For each object, compute and print detector name, date, average, max, and range
- Handle empty-data objects gracefully (`None` / `no data`)

**Hints:**

- Keep formatting consistent for each line
- Compute values once per object, then print

### Check your work

- Do you get one line per object?
- Do empty objects avoid crashing?
- Is your output readable and consistent?

<details>
<summary>Possible Solution for Task 5</summary>

```python
for r in results_list:
    avg = r.get_average_of_results()
    mx = r.get_maximum_of_results()
    rng = r.get_range_of_results()

    if avg is None:
        print(f"{r.detector_name} ({r.date}): no data")
    else:
        print(f"{r.detector_name} ({r.date}): avg={avg}, max={mx}, range={rng}")
```

</details>

---

## Task 6: Add an Extra Analysis Method

Extend the class with one extra method based on your experimental needs.

**Your task:**

- Add at least one extra method, for example:
  - `get_minimum_of_results(self)`
  - `count_results_above(self, threshold)`
  - `has_anomaly(self, threshold)`
- Use your new method in the report output

**Hints:**

- Follow the same empty-list handling pattern as existing methods
- For counting methods, use an explicit counter + `for` loop

### Check your work

- Does your new method return sensible values?
- Does it work on both populated and empty result lists?
- Is the new value shown in your report line?

<details>
<summary>Possible Solution for Task 6</summary>

```python
def count_results_above(self, threshold):
    count = 0
    for value in self.results:
        if value > threshold:
            count += 1
    return count
```

</details>

---

## Task 7 (Optional): Improve `__str__`

Add or improve a `__str__` method so printing an object is useful in your report.

**Hints:**

- Include detector name, date, and maybe number of values
- Keep it one concise line

<details>
<summary>Possible Solution for Task 7</summary>

```python
def __str__(self):
    return f"{self.detector_name} ({self.date}) - {len(self.results)} values"
```

</details>

---

## Example Interaction

```
Detector A (2026-03-03): avg=120.7, max=141, range=43
Detector B (2026-03-03): avg=204.7, max=210, range=11
```

---

**You're done when** your script creates multiple `ResultValue` objects, adds values to each, prints a report (average/max/range), and includes at least one extra analysis method you added.

---

## Key Concepts Demonstrated

- Class instances for domain data (detector/date/results)
- Encapsulation of data + analysis methods
- Lists of objects processed with loops
- Extending classes with new behavior for domain-specific questions

---

## Common Issues

- **Stats return `None` unexpectedly**: Check that you actually called `add_result(...)` before computing stats.
- **`AttributeError` for new method**: Confirm the method is indented inside the class.
- **Class not found**: Make sure the class is defined above the code that creates `ResultValue(...)` objects.
- **Unreadable report output**: Compute values first, then format one clear print line.

---

## Extension Ideas (Optional)

If you finish early, extend only using concepts already in this lab:

1. Add an object with no results and show how your report handles it.
2. Add a second threshold column (e.g. `>150` and `>200`) using your count/anomaly method.
3. Sort your list by detector name before printing (using basic list operations).

---

## Next Steps

In the next lab, you’ll move your class into its own module and import it from a main script.