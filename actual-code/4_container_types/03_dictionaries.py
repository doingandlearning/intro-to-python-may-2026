empty_dict = {}
print(empty_dict)
print(type(empty_dict))

# addressed by key -> key:value pairs

user_dictionary = {
  "name": "Luke",
  "location": "Middlesbrough",
  "degree": "IT",
  "employed": True
}

print(user_dictionary.get("name"))
print(user_dictionary.get("dob", "None of your business"))

print("name" in user_dictionary)
print("Luke" in user_dictionary)

print(list(user_dictionary.keys()))
print(user_dictionary.values())
print(user_dictionary.items())

for value in user_dictionary:
  print(f"For key {value}, the value is {user_dictionary.get(value)}")

for field in user_dictionary.items():
  print(f"For key {field[0]}, the value is {field[1]}")

for key, value in user_dictionary.items():
  print(f"For key {key}, the value is {value}")

print(user_dictionary.pop("name"))
print(user_dictionary)

user_dictionary["name"] = "Luke"
user_dictionary["name"] = "Luke Symmonds"

# JSON -> JavaScipt Object Notation
# {} -> object
# [] -> array
# null -> None
# true -> True
# false -> False

import json

print(json.dumps(user_dictionary))

