# a known amount of things!
for letter in "Kevin Burns":
  print(letter)

user_number = int(input("What number do you want to find?"))

for number in range(1, 100):
  if user_number == number:
    print("Found it!")
    break  # allows me to exit loops early!
  else:
    print(f"It wasn't {number}, still looking!")
else:
  # If you don't break early!
  print("Searched everything. Didn't find!")
  print("All done successfully!.")

# os, re
import random

secret_number = random.randint(1, 50)

for attempt in range(3):
  guess = int(input(f"Attempt {attempt + 1} - enter your guess: "))

  if guess < secret_number:
      print("Too low!")
  elif guess > secret_number:
      print("Too high!")
  else:
      print("Correct!")
      break

print("Hello")