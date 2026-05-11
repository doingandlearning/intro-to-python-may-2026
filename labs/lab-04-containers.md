# Lab 4: Exploring a Playlist Queue with Lists

## Objective

In this lab, you'll get comfortable working with lists, one of the most common data structures in Python. You'll treat a **playlist queue** (tracks waiting to play) as a list of strings and run simple, data-style analysis on those titles.

## Scenario: Playlist Queue Mini-Analysis

Imagine you are inspecting a DJ or streaming queue before a set:

- Start with a list of track titles (each title is one string)
- Count how many tracks are queued and the average number of words per title
- Let someone type a keyword and list every title that matches
- Combine everything into one small script

---

## Task 1: Create a New File

**Your task:** Set up your workspace for this lab.

**What to do:**

1. Create a new Python file called `playlist_queue.py`
2. Think about what you'll need to import (hint: you probably don't need any special imports for this lab)

**Expected outcome:**

- You should have an empty Python file ready to work with
- The file should be named appropriately for this lab

<details>
<summary>Possible Solution for Task 1</summary>

```python
# playlist_queue.py
# (Start with an empty file; import requirements can come later if needed.)
```

</details>

---

## Task 2: Start with a playlist queue

**Your task:** Create a list of track titles to work with.

**What to do:**

1. Create a variable called `queue`
2. Add at least 8–10 track titles to your list
3. Make sure each entry is a string (enclosed in quotes)
4. Mix genres or moods so searches later feel realistic (you can invent titles)

**Hints:**

- Remember that lists use square brackets `[]`
- Each track title should be a separate string
- Titles can be plain text like `Artist Name - Song Title` or a single line describing the track

**Expected outcome:**

- You should have a list with several track titles
- Each item should be a single string
- The queue should feel like something you could scroll through before hitting play

**Check your work:**

- Does your list have enough tracks?
- Are all entries proper strings?
- Is there enough variety that a keyword search could return zero, one, or many matches?

<details>
<summary>Possible Solution for Task 2</summary>

```python
queue = [
    "Fleetwood Mac - The Chain (Live)",
    "Dua Lipa - Training Season",
    "Khruangbin - Time (You and I)",
    "The Smile - Wall of Eyes",
    "Olivia Dean - Dive",
    "LCD Soundsystem - tonite",
    "Jungle - Back On 74",
    "Arlo Parks - Softly (Acoustic)",
    "Bonobo - Kerala",
    "Little Simz - Gorilla",
]
```

</details>

---

## Task 3: Count the tracks and average title length

**Your task:** Compute simple statistics about your queue.

**What to do:**

1. Count how many tracks are in your list
2. Calculate the average number of words per title (words separated by spaces)
3. Display both results in a readable way

**Hints:**

- Think about what tells you how many items are in a list
- To count words, loop over each title and accumulate a running total of words
- The `.split()` method can help you break a string into words
- Initialise a counter for total words before the loop

**Expected outcome:**

- Your program reports how many tracks are in the queue
- It reports the average word count across titles
- Output is easy to read at a glance

**Check your work:**

- Does the track count match `len(queue)`?
- Is the average sensible if you spot-check a few titles by hand?
- Are results formatted clearly?

<details>
<summary>Possible Solution for Task 3</summary>

```python
count = len(queue)
total_words = 0
for title in queue:
    total_words += len(title.split())
average_words = total_words / count

print(f"You have {count} tracks in the queue.")
print(f"Average words per title: {average_words:.2f}")
```

</details>

---

## Task 4: Search the queue by keyword

**Your task:** Let the user search track titles for a keyword.

**What to do:**

1. Ask the user what keyword they want to search for
2. Look through every title in the queue for matches
3. Count how many titles match
4. Print the matching titles and the count

**Hints:**

- Use `input()` to read the search term
- Loop through the queue and test membership in each title
- Consider making the search case-insensitive
- Collect matches in a list if that helps you print them neatly

**Expected outcome:**

- Any keyword can be tried
- Matching titles are listed and the total number of matches is shown
- Capitalisation in the queue does not block a match when the user types different case

**Check your work:**

- Try keywords you know appear in several titles, in one title, and in none
- Does `.lower()` behave the way you expect on both sides of the comparison?
- Is the output easy to scan?

<details>
<summary>Possible Solution for Task 4</summary>

```python
keyword = input("Enter a keyword: ").strip().lower()

matches = []
for title in queue:
    if keyword in title.lower():
        matches.append(title)

print(f"Found {len(matches)} matching tracks:")
for title in matches:
    print("-", title)
```

</details>

---

## Putting It All Together

**Final challenge:** Make sure all parts work together smoothly.

**What to do:**

1. Run the script end-to-end with a few different keywords
2. Confirm counts and averages still look correct after any edits
3. Tidy formatting so statistics and search results are visually separated

**Hints:**

- Test keywords you know are absent as well as present
- Re-check the average calculation if you change the queue
- Blank lines or short headings in the output can help readability

---

## Example Interaction

```
Enter a keyword: live
Found 2 matching tracks:
1. Fleetwood Mac - The Chain (Live)
2. Arlo Parks - Softly (Acoustic)
```

(Your counts will depend on the titles you put in `queue`.)

---

**You're done when** your script can (1) report how many tracks are queued and the average number of words per title, and (2) search titles for a keyword and report how many matches were found.

---

## Key Concepts Demonstrated

- Lists: storing many items in order (the queue)
- Loops: visiting each title
- String helpers such as `.split()` and (optionally) `.lower()`
- Simple search: substring or keyword logic

---

## Check your work

Before moving to the next lab, make sure you can answer these questions:

### Basic Concepts:

- [ ] Can you explain how lists work in Python?
- [ ] Do you understand how to loop through a list?
- [ ] Can you explain what the `.split()` method does?
- [ ] Do you know how to test whether one string appears inside another?

### Practical Skills:

- [ ] Can you create and populate a list with data?
- [ ] Can you calculate simple statistics from list data?
- [ ] Can you search a list of strings for content?
- [ ] Can you combine `input()` with loops and printing?

### If you answered "No" to any questions:

- Review the relevant sections above
- Check the solutions folder for complete code examples
- Ask for help if needed

---

## Common Issues

### Problem: "NameError: name 'queue' is not defined"

**Fix:** Define your `queue` list before you use it in loops or arithmetic.

### Problem: Average word count is zero or clearly wrong

**Fix:** Initialise your running total to zero before the loop and add inside the loop.

### Problem: Search misses obvious matches

**Fix:** Apply `.lower()` consistently to both the stored title and the user's keyword.

### Problem: Program feels fine until there are zero matches

**Fix:** Decide what you want to print when `matches` is empty, and test that branch.

---

## Extension Ideas (Optional)

If you finish early, stay within lists and strings:

1. Print the three longest and three shortest titles by word count.
2. Ask for several keywords separated by commas and report matches per keyword.
3. Print one compact summary block: track count, average words, and match count for the last search.

---

## Next Steps

In the next lab, you'll reorganise similar logic into **functions**, using a different small dataset: bill amounts for a **tip calculator**.

Move on to Lab 5: Functions!

---

## Solutions

**Complete code examples for all exercises are available in the `solutions/` folder.**

- `solutions/playlist_queue.py` — end-to-end playlist queue example
- `solutions/step_by_step/` — individual step solutions

**Try to solve the exercises yourself first, then check the solutions if you get stuck!**

---

## Questions?

If you get stuck or have questions:

1. Read error messages carefully
2. Review the concepts in the notes
3. Look at the solutions folder for examples
4. Ask your instructor or classmates
5. Remember: everyone learns at their own pace!
