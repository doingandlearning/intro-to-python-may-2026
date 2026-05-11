# Lab 8: Organizing Your Code with Modules

## Objective

As your projects grow, putting all your code in one file becomes messy. **Modules** let you split Python across files so responsibilities stay clear.

The aim of this lab is to separate the **`Ticket` class** from the short script that builds example **event tickets** and prints a quick summary.

## Scenario: Modules for event tickets

You will move `Ticket` into `ticket_module.py`, then import it from `main_events.py` so the class can be reused (for example in tests or a larger reporting tool later).

---

## **What are modules?**

A **module** is a Python file you can import. Modules are the building blocks of larger programs.

### **Key Concepts**

- **Module**: file containing importable definitions
- **Import**: reuse code from another file
- **Separation of concerns**: class blueprint vs script that exercises it
- **Reusability**: import the same class from labs, tests, or notebooks

---

## Task 1: Create `ticket_module.py`

### **Tasks**

1. Create a new file named `ticket_module.py`
2. Move the complete `Ticket` class from Lab 7 into this file (`__init__`, `__str__`, `get_segment_count`)
3. Leave out script logic—only the class belongs here

### **Hints**

- Copy the entire `class Ticket:` block with correct indentation
- No sample data, no printing, no `main()` yet—just the blueprint

### **Expected Outcomes**

- Importing `ticket_module` defines `Ticket` without side effects

### **Check Your Work**

- Does the file contain only the class (plus optional module docstring)?
- Can you `import ticket_module` in a REPL without errors?

<details>
<summary>Possible Solution for Task 1</summary>

```python
# ticket_module.py
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

## Task 2: Create `main_events.py`

### **Tasks**

1. Create `main_events.py` alongside `ticket_module.py`
2. Import `Ticket` with `from ticket_module import Ticket`
3. Build a list called `tickets` containing several `Ticket` instances (use realistic codes and venues)
4. Loop through `tickets`, printing each ticket and its segment count

### **Hints**

- Keep imports at the top
- The list can mirror rows you will later load from `events.csv` in Lab 11

### **Expected Outcomes**

- Running `main_events.py` prints one line per ticket plus counts
- Behaviour matches what you had in the single-file class lab, but split across modules

### **Check Your Work**

- Does the import succeed when both files sit in the same directory?
- Is the printed output easy to read?

<details>
<summary>Possible Solution for Task 2</summary>

```python
# main_events.py
from ticket_module import Ticket

tickets = [
    Ticket("EVT-2024-LDN-001", "The O2 London"),
    Ticket("VIP-001", "Royal Albert Hall"),
]

for ticket in tickets:
    print(ticket, "→ segments:", ticket.get_segment_count())
```

</details>

---

## Task 3: Using `if __name__ == "__main__"`

### **Tasks**

1. Wrap the script logic in `def main():`
2. At the bottom of `main_events.py`, add the `if __name__ == "__main__":` guard
3. Call `main()` inside that block

### **Hints**

1. Define `def main():` and indent the list creation + loop inside it  
2. Leave the `if __name__ == "__main__":` block flush left  
3. Import statements usually stay at module level (top), not inside `main()`, unless you have a deliberate reason  

### **Expected Outcomes**

- `python main_events.py` still prints the same results  
- `import main_events` in the REPL does **not** automatically run the loop  

### **Check Your Work**

- Did you remember to call `main()` under the guard?

<details>
<summary>Possible Solution for Task 3</summary>

```python
def main():
    # build tickets, loop, print
    ...

if __name__ == "__main__":
    main()
```

</details>

---

## Example interaction

```
EVT-2024-LDN-001 @ The O2 London → segments: 4
VIP-001 @ Royal Albert Hall → segments: 2
```

(Your venues and counts may differ; match your own data.)

---

**You're done when** `ticket_module.py` holds only `Ticket`, `main_events.py` imports it, defines `main()`, and uses `if __name__ == "__main__"` so imports stay side-effect free.

---

## Key Concepts Demonstrated

- Modules and `from ... import ...`
- Guarded script entry points
- Separating reusable types from throwaway driver code

---

## Common Issues

### **Import errors**

- Filename typos (`ticket_module.py` vs import string)
- Running Python from a different working directory

### **Guard mistakes**

- Accidentally indenting the `if __name__ == "__main__"` block inside `main()`
- Forgetting to call `main()`

---

## **Testing your solutions**

1. Module file contains only the class  
2. Runner imports cleanly  
3. Guard prevents auto-run on import  
4. Printed summaries still make sense  

---

## **Extension ideas (optional)**

- `data_tickets.py` that only builds the sample list, imported by `main_events.py`  
- Helper functions such as `average_segment_count(tickets)` in another module  

---

## **Solutions**

**Reference implementations live in `solutions/lab-08/`.**

- `solutions/ticket_module.py`  
- `solutions/main_events.py`  

---

## Next steps

Lab 9 (error handling) and Lab 10 (pytest) build resilience and confidence. Lab 11 will replace hard-coded ticket rows with rows loaded from **`events.csv`**.

---

## **Why modules?**

They mirror how real Python projects scale: small files, explicit imports, and code you can test in isolation.

---

**Remember**

- One responsibility per file at this stage of learning
- Prefer explicit imports over wildcards
- Re-run your script after each structural change

This pattern is the same whether you are shipping APIs, data jobs, or desktop tools—only the domain changes.
