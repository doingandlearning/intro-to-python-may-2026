# Lab 6: Ticket Codes and List Comprehensions

## Objective

In this lab, you'll use **list comprehensions** to derive new lists from a batch of **ticket codes** in a single, readable line each time. Ticket codes are short strings you might see on event data feeds (often with hyphens separating segments).

---

## Scenario: Ticket codes in one-liners

You have a list of ticket code strings. You want:

- the number of **segments** in each code (segments = parts after splitting on `"-"`)
- only **short** codes (for this lab: at most three segments)
- segment counts for codes whose text contains `"vip"` anywhere, case-insensitive

List comprehensions let you express those transforms compactly.

## **What are List Comprehensions?**

A **list comprehension** is a concise way to build a new list from an existing sequence. Think “for loop in one line,” but keep readability in mind.

### **Key Concepts**

- **Mapping**: apply the same operation to every item
- **Filtering**: keep only items that pass a test
- **Combining**: filter and map together
- **Readability**: prefer a clear comprehension over a clever but cryptic one

---

## Task 1: Getting Started

### **Tasks**

1. Create a new Python file, for example `ticket_code_comprehensions.py`
2. Paste the `ticket_codes` list below into your file
3. Print the list once to confirm it loaded

### **Expected Outcomes**

- A runnable file with the data defined
- You can print all ten codes without error

### **Check Your Work**

- Does the list contain exactly ten strings?
- Are hyphens where you expect them to be?

<details>
<summary>Possible Solution for Task 1</summary>

```python
# ticket_code_comprehensions.py
ticket_codes = [
    "EVT-2024-LDN-001",
    "VIP-001",
    "SUMMER24-FEST-LON-D2",
    "EARLY-BIRD-2024",
    "VIP-GALA-NYC",
    "REG-STANDARD-78901",
    "COMP-FREE-01",
    "BACKSTAGE-VIP-2024",
    "STU-2024-01",
    "PRE-EVT-24-NIGHT",
]
print(ticket_codes)
```

</details>

---

## Task 2: Mapping with list comprehensions

### **Tasks**

1. Create a list called `segment_counts` where each entry is the number of segments in the corresponding ticket code (split on `"-"` and count the pieces)
2. Use a list comprehension
3. Print `segment_counts` to verify

### **Hints**

- Syntax pattern: `[expression for item in sequence]`
- For each code `c`, segment count is `len(c.split("-"))`
- Order of results follows the order of `ticket_codes`

### **Expected Outcomes**

- `segment_counts` has length ten
- Values match the manual counts you expect for the first few codes

### **Check Your Work**

- First code `EVT-2024-LDN-001` should contribute `4`
- Second code `VIP-001` should contribute `2`
- Does the printed list match the verification table later in this lab?

<details>
<summary>Possible Solution for Task 2</summary>

```python
segment_counts = [len(code.split("-")) for code in ticket_codes]
print(segment_counts)
```

</details>

---

## Task 3: Filtering with list comprehensions

### **Tasks**

1. Create `short_codes` containing only codes with **three or fewer** segments
2. Use a comprehension with an `if` clause
3. Print the result

### **Hints**

- Pattern: `[item for item in sequence if condition]`
- Reuse the same segment-count idea inside the condition
- “Short” here means at most three hyphen-separated segments

### **Expected Outcomes**

- `short_codes` is a list of strings
- It should be shorter than the original list (six entries for the provided data)
- Every kept code has at most three segments

### **Check Your Work**

- Manually count segments for one or two codes to build intuition
- Did you use `<= 3` (or equivalent) consistently?

<details>
<summary>Possible Solution for Task 3</summary>

```python
short_codes = [code for code in ticket_codes if len(code.split("-")) <= 3]
print(short_codes)
```

</details>

---

## Task 4: Combining mapping and filtering

### **Tasks**

1. Create `vip_segment_counts`: the segment counts **only** for codes that contain the substring `"vip"` in any casing (`"VIP"`, `"vip"`, etc.)
2. Combine mapping and filtering in one comprehension
3. Print the list

### **Hints**

- Pattern: `[expression for item in sequence if condition]`
- Use `"vip" in item.lower()` (or similar) for the condition
- The expression should still be a segment count, not the raw code

### **Expected Outcomes**

- A list of integers, one per qualifying code
- For the provided data you should pick up every code whose letters include `vip` as a contiguous substring

### **Check Your Work**

- How many codes include `"vip"` when you lower-case them?
- Do the integers match the segment counts of exactly those codes?

<details>
<summary>Possible Solution for Task 4</summary>

```python
vip_segment_counts = [
    len(code.split("-"))
    for code in ticket_codes
    if "vip" in code.lower()
]
print(vip_segment_counts)
```

</details>

---

## Example Interaction

```
segment_counts: [4, 2, 4, 3, 3, 3, 3, 4, 3, 4]
short_codes (<= 3 segments): ['VIP-001', 'EARLY-BIRD-2024', 'VIP-GALA-NYC', 'REG-STANDARD-78901', 'COMP-FREE-01', 'STU-2024-01']
vip_segment_counts: [2, 3, 4]
```

---

**You're done when** all three result lists are produced with comprehensions and the printed numbers match the expectations below.

---

## Key Concepts Demonstrated

- Comprehension syntax with optional `if`
- Mapping structured strings to numeric features (segment counts)
- Case-insensitive substring tests for lightweight data cleaning

---

## Common Issues

### **Syntax errors**

- Missing brackets around the comprehension
- Forgetting the colon after `for` / `if` inside the comprehension (when expanded over multiple lines)

### **Logic errors**

- Miscounting segments because of extra hyphens—split on the exact delimiter you intend
- Forgetting `.lower()` on the ticket code when searching for `"vip"`

### **Empty results**

- If `vip_segment_counts` is empty, re-check the substring test and the spelling of the codes

---

## **Testing your solutions**

### **Reference ticket codes**

1. `EVT-2024-LDN-001` → 4 segments  
2. `VIP-001` → 2  
3. `SUMMER24-FEST-LON-D2` → 4  
4. `EARLY-BIRD-2024` → 3  
5. `VIP-GALA-NYC` → 3  
6. `REG-STANDARD-78901` → 3  
7. `COMP-FREE-01` → 3  
8. `BACKSTAGE-VIP-2024` → 4  
9. `STU-2024-01` → 3  
10. `PRE-EVT-24-NIGHT` → 4  

### **Expected results**

- **Task 2:** `[4, 2, 4, 3, 3, 3, 3, 4, 3, 4]`
- **Task 3:** six codes, each with ≤3 segments (see example interaction)
- **Task 4:** `[2, 3, 4]` — counts for `VIP-001`, `VIP-GALA-NYC`, and `BACKSTAGE-VIP-2024`

---

## **Extension ideas (optional)**

- Codes whose last segment is all digits
- Codes with exactly four segments
- Average segment count across the whole batch (you may compute this outside the comprehension)

---

## **Solutions**

**Complete code examples for all exercises are available in the `solutions/lab-06` folder.**

- `solutions/ticket_code_comprehensions.py`

---

## Next Steps

Next you will bundle code and data into a **`Ticket` class** so each record carries both a code and a venue name.

---

## **Why list comprehensions?**

They help you:

- State transformations plainly
- Avoid bookkeeping lists when a single expression suffices
- Stay close to the language’s idioms for small data shaping tasks

---

**Remember**

- Start simple, then add `if`
- Keep each comprehension readable; split across lines if needed
- Always print intermediate results while learning

This lab links pattern practice to a compact, data-like string format you will reuse when you model `Ticket` objects.
