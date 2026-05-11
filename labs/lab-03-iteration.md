# Lab 3: Iteration and Control Flow

## Objective
In this lab, you'll build a simple guessing game to practice iteration and control flow. You'll use loops, `if/elif/else`, and user input handling to guide a player toward the correct answer.

## Scenario: Channel Number Guessing Game
The program secretly chooses a number for a player to guess:

- The program randomly selects a secret "channel number" between 1 and 50.
- The player has a fixed number of attempts to guess it.
- After each guess, the program tells the player if their guess was too high, too low, or correct.
- The game ends when the player guesses the number or runs out of attempts.

---

## Task 1: Setting up the Game

**Your task:** Set up the basic structure for your guessing game.

**What to do:**

1. Create a new Python file for your game
2. Import the module you need for generating random numbers (`import random`)
3. Create a variable to store the secret channel number
4. Print a welcome message explaining the game rules

**Hints:**

- Look up how to generate a random integer between 1 and 50
- Make your welcome message clear and friendly
- Tell the player how many attempts they have

**Expected outcome:**

- Your program should generate a random number when it runs
- It should display a welcome message explaining the rules
- The secret number should be different each time you run the program

**Check your work:**

- Run the program multiple times - does the secret number change?
- Is your welcome message clear and helpful?
- Does the program run without errors?

<details>
<summary>Possible Solution for Task 1</summary>

```python
import random

secret_number = random.randint(1, 50)
print("Welcome to the Channel Guessing Game!")
print("I'm thinking of a number between 1 and 50.")
attempts = 5
print(f"You have {attempts} attempts.")
```

</details>

---

## Task 2: The Game Loop

**Your task:** Create a loop that gives the player multiple attempts to guess.

**What to do:**

1. Decide how many attempts the player should have
2. Create a loop that runs that many times
3. Think about what type of loop would work best for this

**Hints:**

- You know exactly how many attempts the player gets, so what type of loop makes sense?
- Remember that `range(5)` gives you numbers 0, 1, 2, 3, 4
- All the game logic will go inside this loop

**Expected outcome:**

- Your program should loop the correct number of times
- The loop should be ready to contain the guessing logic

**Check your work:**

- Does your loop run the right number of times?
- Is the loop structure clear and readable?

<details>
<summary>Possible Solution for Task 2</summary>

```python
for attempt in range(attempts):
    # put your guess-checking code inside this loop
    pass
```

</details>

---

## Task 3: Getting and Checking the User's Guess

**Your task:** Add the core game logic inside your loop.

**What to do:**

1. Ask the user for their guess inside the loop
2. Convert their input to a number
3. Compare their guess to the secret number
4. Give them appropriate feedback
5. Handle the case when they guess correctly

**Hints:**

- Remember that `input()` gives you a string - you need to convert it
- Think about the three possible outcomes: too low, too high, or correct
- What should happen when they guess correctly? How do you exit the loop early?
- Make your feedback messages helpful and encouraging

**Expected outcome:**

- Players should be able to input their guesses
- They should get clear feedback after each guess
- The game should end immediately if they guess correctly

**Check your work:**

- Try guessing too low, too high, and correctly
- Are your feedback messages clear and helpful?
- Does the game end when you guess correctly?

<details>
<summary>Possible Solution for Task 3</summary>

```python
guess = int(input(f"Attempt {attempt + 1} - enter your guess: "))

if guess < secret_number:
    print("Too low!")
elif guess > secret_number:
    print("Too high!")
else:
    print("Correct!")
    break
```

</details>

---

## Task 4: Handling a Win or Loss

**Your task:** Determine the final outcome and display appropriate messages.

**What to do:**

1. Figure out how to tell if the player won or lost
2. Display different messages for winning vs. losing
3. If they lost, show them what the secret number was

**Hints:**

- Think about how you can track whether the player has won
- What happens if the loop finishes without a correct guess?
- How can you tell the difference between winning and losing?

**Expected outcome:**

- Winners should get a congratulatory message
- Losers should see what the secret number was
- The game should clearly indicate the final result

**Check your work:**

- Test both winning and losing scenarios
- Are the final messages clear and appropriate?
- Does the program handle both outcomes correctly?

<details>
<summary>Possible Solution for Task 4</summary>

```python
won = False  # set to True when the guess is correct

# ... inside Task 3 correct branch: won = True

if won:
    print("You guessed the secret number! Congratulations.")
else:
    print(f"Out of attempts. The secret number was {secret_number}.")
```

</details>

---

## Putting It All Together

**Final challenge:** Make sure all parts work together smoothly.

**What to do:**

1. Test your complete game multiple times
2. Try different strategies (guessing high, low, or in the middle)
3. Make sure the game works whether you win or lose
4. Add any finishing touches to make it more polished

**Hints:**

- Test edge cases (guessing 1, guessing 50, etc.)
- Make sure your messages are consistent and helpful
- Consider adding some personality to your game

---

## Example Interaction

```
Welcome to the Channel Guessing Game!
You have 5 attempts to guess the secret number (between 1 and 50).

Attempt 1 - enter your guess: 10
Too low!

Attempt 2 - enter your guess: 30
Too high!

Attempt 3 - enter your guess: 25
Correct! You guessed the secret number!
```

---

**You're done when** your program lets a player enter guesses, gives “too low / too high / correct” feedback, and stops immediately when the player guesses correctly (or prints the secret number when attempts run out).

---

## Key Concepts Demonstrated

- `for`/`while` loops: repeating a section of code multiple times
- `range(...)`: controlling how many attempts the player gets
- `if/elif/else`: comparing guesses to the secret number
- `break`: exiting a loop early when the player wins
- `input()` + type conversion: turning user input text into a number

---

## Check your work

Before moving to the next lab, make sure you can answer these questions:

### Basic Concepts:

- [ ] Can you explain how a `for` loop works?
- [ ] Do you understand the difference between `if`, `elif`, and `else`?
- [ ] Can you explain what the `break` statement does?
- [ ] Do you know how to generate random numbers?

### Practical Skills:

- [ ] Can you create a program that loops a specific number of times?
- [ ] Can you handle different user inputs and give appropriate responses?
- [ ] Can you create a program that tracks game state?
- [ ] Do you understand how to exit a loop early?

### If you answered "No" to any questions:

- Review the relevant sections above
- Check the solutions folder for complete code examples
- Ask for help if needed

---

## Common Issues

### Problem: "NameError: name 'random' is not defined"

**Fix:** Make sure you've imported the `random` module at the top of your file.

### Problem: "ValueError: invalid literal for int()"

**Fix:** The user entered something that's not a number. Think about how to handle this gracefully.

### Problem: Game doesn't end when guessing correctly

**Fix:** Make sure you're using `break` when the guess is correct.

### Problem: Loop runs too many or too few times

**Fix:** Check your `range()` function - remember it starts at 0.

---

## Extension Ideas (Optional)
If you finish early, extend the same guessing-game logic:

1. Add a “distance hint”: after each guess, print whether the guess is within (for example) 5 numbers of the secret.
2. Let the player choose the number of attempts at the start (still using loops and the same feedback messages).
3. Track and print how many guesses the player took when they win.

---

## Next Steps

In the next lab, you'll learn about:

- Working with lists and other container types
- More complex data structures
- Processing collections of data

Move on to Lab 4: Container Types!

---

## Solutions

**Complete code examples for all exercises are available in the `solutions/` folder.**

- `solutions/guessing_game.py` - Complete game solution
- `solutions/step_by_step/` - Individual step solutions

**Try to solve the exercises yourself first, then check the solutions if you get stuck!**

---

## Questions?

If you get stuck or have questions:

1. Check the error messages carefully
2. Review the concepts in the notes
3. Look at the solutions folder for examples
4. Ask for help from your instructor or classmates
5. Remember: everyone learns at their own pace!
