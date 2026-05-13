def get_a_number_from_user():
  try:
    result = int(input("Give me a number: "))
    return result
  except ValueError:
    print("That's a valid number, try again.")
    return get_a_number_from_user()

print(get_a_number_from_user())

class Customer:
  def __init__(self, name, contact_email):
    if len(name) == 0:
      raise ValueError("You need to give me a name.")
    self.name = name
    self.contact_email = contact_email

  def send_confirmation(self, booking):
    print(f"Sending {booking} confirmation to {self.contact_email}")

cust1 = None

while cust1 is None:
  try: 
    name = input("Give me name: ")
    cust1 = Customer(name, "") 
  except ValueError as e:
    print(e)