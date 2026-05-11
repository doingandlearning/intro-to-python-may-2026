age = 13
is_teenager = None  # placeholder
if age > 12 and age < 20:
  is_teenager = True
else:
  is_teenager = False

# if expressions -> concise
is_teenager = True if age > 12 and age < 20 else False

if is_teenager is None:
  print("hasn't been updated!")
else:
  print(f"{is_teenager}")


