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

v = Vehicle(registration=None, make="Ford", model="Transit", 
            year="two thousand and twenty", max_payload_kg=-500, status="Available")
print(v.is_available())