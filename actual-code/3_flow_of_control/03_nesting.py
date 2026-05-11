port = "SOU"
ship = "12311"
dest = "NYC"


# Do as little nesting as you can!


if port == "SOU":
  print("Didn't do too well with the Titanic")
  if ship == "12312":
    print("This is a good ship")
    if dest == "NYC":
      print("That's a long crossing")
  else:
    print("Not ship 12321")
else:
  print("Not Southampton")