user_input = input("What's the password? ")
password = "password123"

# unknown number of times!
# while this is true
while user_input != password:  # infinite loop!  Ctrl-C
  print("Invalid password")
  user_input = input("What's the password? ")

print("Here are your secret documents.")

counter = 1

while counter < 10:
  print(counter)
  counter += 1
  # counter = counter + 1