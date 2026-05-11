user_number = int(input("Give me a number: "))

# <  >  <=  >=  !=
if user_number == 42:
  # block of code -> if block
  print("That is the right answer.")
  print("This is cool")
elif user_number == 67:     # (else if)
  print("are you a gen alpha meme?")
elif user_number == 21:
  print("You can drink in the US now.")
else:
  print("That was wrong - try again!")


match user_number:
  case 42:
    print("That's right!")
  case 67:
    print("Meme!")
  case 21:
    print("Drink in US")
  case _:
    print("All wrong!")