class Vehicle:
  def __init__(self, registration, make, model, year, max_payload_kg, status="Available"):
    if not isinstance(year, int):
      raise TypeError(f"year must be an int, got {type(year).__name__}")

    if max_payload_kg <= 0 or max_payload_kg > 10000:
      raise ValueError(f"max_payload_kg must be positive and less than 10000, got {max_payload_kg}")

    if not registration: # None or ""
      raise ValueError("registration is required")

    self.registration = registration
    self.make = make
    self.model = model
    self.year = year
    self.max_payload_kg = max_payload_kg
    self.status = status
    self.driver_id = None

  def __repr__(self):
    return f"Vehicle(registration={self.registration})"

  def to_dict(self):
    return {"registration": self.registration,
            "make": self.make,
            "model": self.model,
            "year": self.year,
            "max_payload_kg": self.max_payload_kg,
            "status": self.status}

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
