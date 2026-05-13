# Lab 11: Reading Data From a File

## Objective

Hard-coded lists are fine while learning, but real programs usually **load** datasets from disk. In this lab you will read event ticket rows from **`events.csv`** using Python’s built-in `csv` module and turn each row into a `Ticket` instance.

---

## Scenario: Loading events from CSV

Instead of pasting ticket rows into `main_events.py`, you will open `events.csv`, skip the header, build `Ticket` objects (`code`, `venue`), append them to a list, and reuse whatever summary logic you already wrote after the modules lab.

---

## **What is file I/O?**

**File I/O** means reading from or writing to files. CSV is a common text format for tabular data: one row per line, columns separated by commas.

### **Key Concepts**

- Opening files safely with context managers  
- `csv.reader` for row-wise parsing  
- Skipping header rows  
- Turning each row’s strings into structured objects (`Ticket`)  
- Keeping “load data” separate from “analyse data”  

---

## Task 1: Getting Started

### **Tasks**

1. Import the `csv` module at the top of `main_events.py` (or your chosen runner)
2. Inside `main()`, prepare an empty list, for example `tickets = []`
3. Remove or comment out any hard-coded `tickets = [...]` list from earlier labs
4. Confirm `events.csv` sits next to your script when you run it

### **Hints**

- You are evolving the script from Lab 8, not starting from scratch
- Paths are relative to your current working directory when you launch Python

### **Expected Outcomes**

- `import csv` is present
- An empty `tickets` list exists before you read the file
- No duplicate hard-coded data remains unless you commented it for reference

### **Check Your Work**

- Does the CSV file appear beside `main_events.py` in the file tree?
- Did you avoid deleting the `Ticket` import?

<details>
<summary>Possible Solution for Task 1</summary>

```python
import csv

# either import if you have it
from ticket_module import Ticket

# or use it directly
class Ticket:
    def __init__(self, code, venue):
        self.code = code
        self.venue = venue

    def __str__(self):
        return f"{self.code} @ {self.venue}"

    def get_segment_count(self):
        return len(self.code.split("-"))

def main():
    tickets = []
    # Remove/comment the old hard-coded tickets = [Ticket(...), ...]
    ...

if __name__ == "__main__":
    main()
```

</details>

---

## Task 2: Open and read the file

### **Tasks**

1. Open `events.csv` with `with open(..., newline="", encoding="utf-8")`
2. Construct a `csv.reader`
3. Skip the header row (`next(reader)` is the usual approach)
4. Iterate over the remaining rows inside `main()`

### **Hints**

- Mode `"r"` for reading text  
- `newline=""` avoids surprising CSV behaviour on some platforms  
- Each `row` is a list of strings, e.g. `["EVT-2024-LDN-001", "The O2 London"]`

### **Expected Outcomes**

- No exceptions when opening the bundled `events.csv`
- Loop runs once per data row (ten tickets in the provided file)

### **Check Your Work**

- Print `row` temporarily if you need to see the raw structure
- Confirm the header line is not processed as data

<details>
<summary>Possible Solution for Task 2</summary>

```python
with open("events.csv", "r", newline="", encoding="utf-8") as f:
    reader = csv.reader(f)
    next(reader)  # skip header: code,venue

    for row in reader:
        # row[0] is code, row[1] is venue
        pass
```

</details>

---

## Task 3: Create objects from file data

### **Tasks**

1. Read `code` from `row[0]` and `venue` from `row[1]`
2. Instantiate `Ticket(code, venue)`
3. Append each instance to `tickets`
4. After the loop, run your reporting logic (print each ticket, average segment count, etc.)

### **Hints**

- Validate mentally that every data row has two columns  
- If a row is malformed, decide whether to skip it or stop—start strict, then relax later  

### **Expected Outcomes**

- `len(tickets)` matches the number of data rows (ten in the sample file)
- Printing matches what you saw when the data was hard-coded

### **Check Your Work**

- Spot-check the first row against the CSV in your editor
- Does `Ticket.get_segment_count()` still behave as expected?

<details>
<summary>Possible Solution for Task 3</summary>

```python
for row in reader:
    code = row[0]
    venue = row[1]
    tickets.append(Ticket(code, venue))
```

</details>

---

## Example interaction

```
Loaded 10 tickets from events.csv
EVT-2024-LDN-001 @ The O2 London → segments: 4
...
```

---

**You're done when** your program reads `events.csv`, converts each row into a `Ticket`, and downstream logic uses the `tickets` list exactly as before—without an inline copy of the dataset.

---

## Key Concepts Demonstrated

- `with open(...)` context managers  
- `csv.reader`, headers, and iteration  
- Bridging file rows → objects  
- Separation between I/O code and domain logic  

---

## Common Issues

### **File handling**

- Wrong working directory → file not found  
- Missing `newline=""` causing odd newline parsing on Windows  

### **CSV structure**

- Forgetting to skip the header (double-counting or wrong types)  
- Extra commas in a field without quoting (not an issue in the provided file, but watch for it in the wild)  

### **Object creation**

- Indices off by one (`row[1]` vs `row[0]`)  
- Trailing blank lines producing empty rows—decide how to handle them  

---

## **Testing your solutions**

1. File opens cleanly  
2. Header skipped  
3. Ten `Ticket` instances for the bundled CSV  
4. Summary output matches expectations  

---

## **Extension ideas (optional)**

- Wrap file access in `try` / `except FileNotFoundError`  
- Strip whitespace from each cell (`strip()`) before constructing `Ticket`  
- Skip rows that do not contain exactly two columns  

---

## **Running your program**

- Ensure `events.csv` is beside `main_events.py`  
- Run `python main_events.py` (or use your editor’s Run button)  
- Optionally print `len(tickets)` right after loading  

---

## **Why file I/O?**

Data files let analysts refresh inputs without touching code, which is how most production pipelines evolve.

---

## Next steps

Try combining this loader with defensive checks from the error-handling lab: validate rows before constructing `Ticket` objects.

---

## **Solutions**

**Worked examples live in `solutions/lab-11/`.**

- `solutions/main_events_with_csv.py` (name may vary—check the folder)  
- `solutions/step_by_step/`  

---

**Remember**

- Keep loaders small and testable  
- Treat everything that comes from CSV as text until you convert it  
- Re-run after moving files—paths are easy to break accidentally  

You now have the same modular structure as before, but the dataset lives outside your Python file where operations teams expect it.
