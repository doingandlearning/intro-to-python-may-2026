def print_message_with_borders(message, border_symbol="=", border_length=10):
  """
  Prints a message with borders. You can change the border symbol and length.
  """
  print(border_symbol * border_length)
  print(message)
  print(border_symbol * border_length)

class Vehicle:
  def __init__(self, registration, make, model, year, max_payload_kg, status="Available"):
    self.registration = registration
    self.make = make
    self.model = model
    self.year = year
    self.max_payload_kg = max_payload_kg
    self.status = status
    self.driver_id = None

  def __repr__(self):
    return f"Vehicle(registration={self.registration})"

  def assign_driver(self, driver_id):
    if self.status != "Available":
      return False
    self.status = "In use"
    self.driver_id = driver_id
    return True

  def release_driver(self):
    self.driver_id = None
    self.status = "Available"

  def is_available(self):
    return self.status == "Available"


truck = Vehicle(registration="", make="", model="", year=1211, max_payload_kg=1000)

if __name__ == "__main__":
  print("Hello from the utils module!")
  print(f"I am {__name__}")