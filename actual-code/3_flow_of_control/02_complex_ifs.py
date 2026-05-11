user_input = input("Shipping container ref: ").upper().strip()
# GOT123   SOU123   BEL12319  LIV12312

# as specific possible
if user_input.startswith("GOT"):
  print(f"Point of origin: Gothemburg, Container Number: {user_input[3:]}")
elif user_input.startswith("SOU") or user_input.startswith("LIV"):
  print("Point of origin: England")
elif user_input.startswith("BEL") and user_input.endswith("9"):
  print("Valid container for BEL")
# as general
if not user_input.startswith("LON"):
  print("Not from Londo")
else:
  print("Not a valid point of origin")
