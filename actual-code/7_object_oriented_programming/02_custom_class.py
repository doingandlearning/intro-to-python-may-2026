truck = {
  "registration": "AGZ 1234",
  "make": "Ford",
  "model": "Transit",
  "year": 2020,
  "max_payload_kg": 7000,
  "status": "available"
}

truck_2 = {
  "reg": "AHR 4321"
}

class Vehicle:
  def __init__(self, registration, make, model, year, max_payload_kg, status):
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
    
# PyObject -> is it assigned variable? -> 



# initialised/created/instantiated/construct
truck = Vehicle(registration="AGZ 1234",
                make="Ford", 
                model="Transit",
                max_payload_kg=7000,
                status="Available",
                year=2020
                ) 

print(truck.registration)
print(truck.year)
print(truck)

print(truck.status)
truck.assign_driver(123)
truck.assign_driver(321)
print(truck.status)
print(truck.driver_id)

truck.release_driver()
truck.assign_driver(456)
print(truck.status)
print(truck.driver_id)

trucks = [Vehicle(registration="AGZ 1234",
                make="Ford", 
                model="Transit",
                max_payload_kg=7000,
                status="Available",
                year=2020
                ),Vehicle(registration="AGZ 1235",
                make="Ford", 
                model="Transit",
                max_payload_kg=7000,
                status="Available",
                year=2020
                ) ,Vehicle(registration="AGZ 1236",
                make="Ford", 
                model="Transit",
                max_payload_kg=7000,
                status="Available",
                year=2020
                ) ,Vehicle(registration="AGZ 1237",
                make="Ford", 
                model="Transit",
                max_payload_kg=7000,
                status="Available",
                year=2020
                ) ]

trucks[0].assign_driver(123)
trucks[1].assign_driver(456)

print([truck for truck in trucks if truck.is_available()])




class Customer:
  ...

class PAndO(Customer):
  pass