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