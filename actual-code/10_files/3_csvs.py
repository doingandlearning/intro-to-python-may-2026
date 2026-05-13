import csv
from vehicle import Vehicle

vehicles = []
with open("10_files/vehicles.csv") as file:
  # reader = csv.reader(file) # loads each row as a list
  reader = csv.DictReader(file) # loads each row as a list
  # for registration, make, model, year, max_payload_kg, status in reader:
  for row in reader:
    try:
      v = Vehicle(registration=row.get("registration"), 
                  make=row.get("make"), 
                  model=row.get("model"), 
                  year=int(row.get("year", "")), 
                  max_payload_kg=int(row.get("max_payload_kg", "")), 
                  status=row.get("status", ""))
      vehicles.append(v)
    except (ValueError, TypeError) as e:
      print(f"Skipping invalid vehicle: {e} from this row: {row}")

print(vehicles)


with open("10_files/vehicles.csv", mode="a", newline="") as file:
  v = Vehicle(registration="HG13 HYS", make="BMW", model="Sprinter", year=2023, max_payload_kg=1000, status="Available")
  writer = csv.DictWriter(file, fieldnames=["registration", "make", "model", "year", "max_payload_kg", "status"])
  writer.writerow(v.to_dict())


available_vehicle = [v for v in vehicles if v.is_available()]
print(available_vehicle.pop())