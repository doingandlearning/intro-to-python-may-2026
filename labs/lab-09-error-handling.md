# Lab 9: The Fault-Tolerant Checkout

## Objective

Build a tiny checkout that **never crashes**, even when the user enters nonsense. It should keep asking until it gets valid input, and give clear feedback.

You’ll practise:

- `try...except`
- handling _different_ error types
- validating ranges
- using `continue`
- (optional) separating input logic into a helper function

## Scenario: A Checkout That Must Keep Working
You’re building a small command-line checkout app. Users will type things (and sometimes they will type garbage), so your job is to keep the program running by handling parsing errors and validating ranges.

---

## Setup

Start a new file: `lab_09_checkout.py`

Your program sells 5 items:

- `"Coffee"` costs £3.50
- `"Tea"` costs £2.40
- `"Sandwich"` costs £5.95
- `"Cake"` costs £3.25
- `"Fruit"` costs £1.10

The user will:

1. choose an item by number
2. enter a quantity
3. repeat until they type `done`
4. see a receipt and total

---

## Task 1: Get it working (no error handling yet)

### Your task

- Print the menu (numbered 1–5)
- Ask for an item number
- Ask for a quantity
- Add line total to a running total
- Let the user type `done` to finish (at the item prompt)

### Outcome

A working checkout that crashes if input is bad.

<details>
<summary>Possible Solution for Task 1 (starter program)</summary>

```python
items = [
    {"id": 1, "name": "Coffee",   "price": 3.50},
    {"id": 2, "name": "Tea",      "price": 2.40},
    {"id": 3, "name": "Sandwich", "price": 5.95},
    {"id": 4, "name": "Cake",     "price": 3.25},
    {"id": 5, "name": "Fruit",    "price": 1.10},
]

total = 0.0
purchases = []  # You will use this later for the receipt (Task 4)

print("Welcome to the Fault-Tolerant Checkout")
print("Type 'done' at any time at the item prompt to finish.\n")

while True:
    print("Menu:")
    for item in items:
        print(f"  {item['id']}. {item['name']} (£{item['price']:.2f})")

    choice = input("\nChoose an item number (1-5) or type 'done': ").strip().lower()
    if choice == "done":
        break

    # Step 1: This will crash on invalid input. You'll fix that in Step 2.
    choice_num = int(choice)

    # Find the chosen item
    chosen_item = None
    for item in items:
        if item["id"] == choice_num:
            chosen_item = item
            break

    if chosen_item is None:
        print("That item number doesn't exist.\n")
        continue

    qty_text = input(f"How many {chosen_item['name']}? ").strip()

    # Step 1: This will crash on invalid input. You'll fix that in Step 2.
    quantity = int(qty_text)

    line_total = chosen_item["price"] * quantity
    total += line_total

    # We'll build a proper receipt in Step 4
    print(f"Added: {chosen_item['name']} x{quantity} = £{line_total:.2f}")
    print(f"Running total: £{total:.2f}\n")

print("\nThanks! (Receipt comes in Step 4)")
print(f"Total: £{total:.2f}")
```

</details>

---

## Task 2: Stop crashes from bad numbers

### Your task

Wrap the risky conversions in `try...except` so the program **never crashes** when:

- the user types text instead of a number (`ValueError`)
- the user just presses Enter
- the user types something like `3.5` for a menu choice

### Rules

- If the menu choice is invalid, show a helpful message and re-prompt.
- If the quantity is invalid, show a helpful message and re-prompt.

### Outcome

Users can type anything and the program keeps going.

<details>
<summary>Possible Solution for Task 2</summary>

```python
# Wrap the parsing in try/except so you can continue looping.
try:
    choice_num = int(choice)
except ValueError:
    print("Menu choice must be a whole number.\n")
    continue

try:
    quantity = int(qty_text)
except ValueError:
    print("Quantity must be a whole number.\n")
    continue
```

</details>

---

## Task 3: Validate ranges and meaning

Error handling catches “can’t parse”, but not “doesn’t make sense”.

### Your task

Add checks so that:

- menu choice must be 1–5
- quantity must be an integer >= 1
- optionally: quantity must be <= 20 (to prevent typos like 2000)

If a check fails:

- print a specific message
- `continue` the loop

### Outcome

The checkout is robust and sensible.

<details>
<summary>Possible Solution for Task 3</summary>

```python
# After you've parsed choice_num and quantity:
if choice_num < 1 or choice_num > 5:
    print("Choose a menu number between 1 and 5.\n")
    continue

if quantity < 1:
    print("Quantity must be >= 1.\n")
    continue

if quantity > 20:  # optional cap to avoid typos
    print("Quantity is too large (max 20).\n")
    continue
```

</details>

---

## Task 4: Produce a receipt

### Your task

Store each purchase in a list so you can print a receipt at the end.

Each purchase should include:

- item name
- unit price
- quantity
- line total

### Outcome

At the end, print something like:

- Coffee x2 = £7.00
- Cake x1 = £3.25
  Total = £10.25

<details>
<summary>Possible Solution for Task 4</summary>

```python
# While looping, store each purchase.
# Example shape of each entry:
# {"name": ..., "unit_price": ..., "quantity": ..., "line_total": ...}
purchases.append({
    "name": chosen_item["name"],
    "unit_price": chosen_item["price"],
    "quantity": quantity,
    "line_total": line_total,
})

# After the loop, print a simple receipt from `purchases`.
for p in purchases:
    print(f"{p['name']} x{p['quantity']} = £{p['line_total']:.2f}")
```

</details>

---

## Task 5: Add one “real world” feature (pick one)

Pick **one**:

### Option A: Discount codes

At the end ask:

- “Enter discount code or press Enter:”
  Valid codes:
- `SAVE10` → 10% off total
- `FIVER` → £5 off (but never below £0)

Handle invalid codes gracefully.

### Option B: Remove last item

If the user types `undo` at the item prompt:

- remove the last purchase (if there is one)
- print what you removed

### Option C: Split bill

Ask:

- “How many people?” (must be integer >=1)
  Print per-person cost.

<details>
<summary>Possible Solution for Task 5</summary>

```python
# Example (Option A - discount codes):
code = input("Enter discount code or press Enter: ").strip().upper()

if code == "SAVE10":
    discount = 0.10 * total
elif code == "FIVER":
    discount = min(5.00, total)
else:
    discount = 0.0  # invalid/blank code

total = max(0.0, total - discount)
```

</details>

---

## Example Interaction

```
Choose an item number (1-5) or type 'done': hello
Menu choice must be a whole number.

Choose an item number (1-5) or type 'done': 2
How many Tea? ten
Quantity must be a whole number.
```

---

**You're done when** your checkout never crashes on bad input, validates item numbers and quantities, loops until `done`, and prints a sensible total/receipt.

---

## Key Concepts Demonstrated

- `try...except` with `ValueError`
- Range checks + `continue` to re-prompt
- Building a `purchases` list for a receipt
- Optional features based on extra user input

---

## Check your work

### Testing scenarios

Try these inputs during the lab:

- menu: `hello`
- menu: `0`
- menu: `6`
- menu: `2.2`
- menu: `` (just Enter)
- quantity: `-1`
- quantity: `0`
- quantity: `ten`
- quantity: `3.5`
- flow: valid purchase → invalid purchase → valid purchase → done

Expected:

- no crashes
- clear messages
- you can always recover and continue

---

## Common Issues

- Catching `except:` instead of specific exceptions
- Putting _too much_ inside `try` (keep it minimal)
- Forgetting to `continue` after an error
- Handling parse errors but forgetting range validation

---

## Next Steps
In the next lab, you'll learn how to lock in behavior with automated tests using `pytest`.

---

## Extension ideas (if you want stretch goals)

- Allow item name input (“coffee”) as well as number
- If they buy the same item twice, merge the quantities
- Show running total after each add
