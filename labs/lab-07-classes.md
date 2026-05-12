# Lab 7: Structuring Data with Classes

## Objective

So far, ticket-style records have been plain strings (or parallel lists). As fields accumulate—**code**, **venue**, and rules about the code itself—**classes** help you keep data and behaviour in one place.

The aim of this lab is to create a `Ticket` class with a ticket **code** and **venue**, then add helpers such as a readable string form and a **segment count** (same idea as Lab 6: split on `"-"`).

## Scenario: Ticket objects

You will represent each admission record as a `Ticket` object (`code` + `venue`) and attach small methods that answer common questions about the code string.

---

## Starter code

This covers step 1 and should give you a running start.

<details>
  <summary>Starter code</summary>
  
```python
class Ticket:
    def __init__(self, code, venue):
        self.code = code
        self.venue = venue

t = Ticket(
    "EVT-2024-LDN-001",
    "The O2 London",
)
```

</details>

---

## Task 1: Defining the `Ticket` class

### **Tasks**

1. Create a new Python file, for example `ticket_objects.py`
2. Define a class named `Ticket`
3. Add a constructor (`__init__`) that accepts `code` and `venue`
4. Store both values on `self`

### **Hints**

- Start with `class Ticket:`
- Constructor signature: `def __init__(self, code, venue):`
- Typical pattern: `self.code = code` and `self.venue = venue`
- `self` always refers to the instance being built

### **Expected Outcomes**

- You can construct `Ticket("VIP-001", "Royal Albert Hall")`
- Attributes are accessible with dot notation

### **Check Your Work**

- Does `Ticket("TEST-CODE", "Test Venue")` run without errors?
- Can you read `.code` and `.venue` on the instance?

<details>
  <summary>Possible Solution for Task 1</summary>

```python
class Ticket:
    def __init__(self, code, venue):
        self.code = code
        self.venue = venue
```

</details>

---

## Task 2: Adding a string representation

### **Tasks**

1. Implement `__str__(self)` on `Ticket`
2. Return a concise human-readable line (code plus venue is enough)
3. Verify with `print(...)`

### **Hints**

- Signature inside the class: `def __str__(self):`
- Must `return` a string; f-strings are convenient
- After implementing, `print(t)` should look intentional, not like `<Ticket object ...>`

<details>
  <summary>Possible solution</summary>

```python
def __str__(self):
    return f"{self.code} @ {self.venue}"

print(t)
```

</details>

### **Expected Outcomes**

- Printing an instance shows both code and venue clearly

### **Check Your Work**

- Does the output match the format you want to standardise on?
- Try a second instance with different data

---

## Task 3: Behaviour with a method

### **Tasks**

1. Add `get_segment_count(self)` to `Ticket`
2. Return how many segments the code has when split on `"-"` (same rule as Lab 6)
3. Call the method on a few instances

### **Hints**

- Method header: `def get_segment_count(self):`
- Use `self.code` inside the method body
- Returning `len(self.code.split("-"))` matches the comprehension lab

<details>
  <summary>Possible solution</summary>

```python
def get_segment_count(self):
    return len(self.code.split("-"))

print(t.get_segment_count())
```

</details>

### **Expected Outcomes**

- Known codes return the counts you expect (for example four segments on `EVT-2024-LDN-001`)

### **Check Your Work**

- Does `get_segment_count()` ignore the venue (only the code should matter)?
- Does it behave for short codes like `VIP-001`?

---

## Task 4: Refactoring to a list of objects (optional / extension)

### **Tasks**

1. Build a list of several `Ticket` instances with different codes and venues
2. Loop through the list printing each ticket’s `__str__` output and segment count
3. Compare this organisation to keeping two separate lists in parallel

### **Hints**

- Instantiate with real-looking codes from Lab 6 if you want continuity
- Call `get_segment_count()` inside the loop

### **Expected Outcomes**

- A short script that demonstrates batch processing of structured records

### **Check Your Work**

- Is it obvious which venue belongs to which code when you read the loop?

<details>
  <summary>Possible solution for Task 4</summary>

```python
tickets = [
    Ticket("EVT-2024-LDN-001", "The O2 London"),
    Ticket("VIP-GALA-NYC", "Brooklyn Steel"),
    Ticket("STU-2024-01", "O2 Academy Brixton"),
]

for ticket in tickets:
    print(ticket)
    print(f"Segment count: {ticket.get_segment_count()}")
    print()
```

</details>

---

## Example interaction

```
EVT-2024-LDN-001 @ The O2 London
Segment count: 4
```

---

**You're done when** your `Ticket` class stores `code` and `venue`, implements `__str__`, and exposes `get_segment_count()` that matches the hyphen-splitting rule from the previous lab.

---

## Key Concepts Demonstrated

- Classes bundle data with behaviour
- Attributes live on `self`
- Special methods: `__init__`, `__str__`
- Ordinary methods encapsulate small calculations

---

## Common Issues

### **Class definition**

- Missing colon after `class Ticket`
- Methods not indented under the class
- Forgetting `self` as the first parameter

### **Constructor mistakes**

- Typos in attribute names
- Parameters passed in the wrong order when constructing instances

### **Method mistakes**

- `__str__` that prints instead of returning
- Using a bare variable name instead of `self.code`

---

## **Testing your solutions**

### **Sample instances**

- `EVT-2024-LDN-001` at `The O2 London`
- `VIP-GALA-NYC` at `Brooklyn Steel`
- `STU-2024-01` at `O2 Academy Brixton`

### **Scenarios to try**

1. Construction with varied venues  
2. Attribute access  
3. Readable `print` output  
4. Segment counts for short and long codes  
5. Looping over a list of `Ticket` objects  

---

## **Extension ideas (optional)**

- `is_short_code(max_segments)` returning `True` when segment count is small  
- `contains_token(token)` doing a case-insensitive substring search on `self.code`  
- `display_label()` returning a title-case venue string while keeping the raw code  

---

## **Solutions**

**Complete code examples for all exercises are available in the `solutions/lab-07` folder.**

- `solutions/ticket_objects.py`

---

## Next steps

Lab 8 moves the class into its own **module** and keeps a small runner script separate.

---

## **Why classes?**

They reduce the mental overhead of “which list index lines up with which?” and give you a single place to adjust behaviour when the data rules change.

---

**Remember**

- Keep methods focused
- Prefer clear names (`code`, `venue`, `get_segment_count`)
- Test with both typical and edge-case codes

Some people find classes abstract at first—that is normal; the goal here is a tiny, concrete type you can hold in your head in one glance.
