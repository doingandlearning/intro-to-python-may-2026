empty_list = []
empty_list = list()

beatles = ["John", "Paul", "George", "Ringo"]
print(len(beatles))
print(beatles)

# CRUD 
# Create
beatles.append("Kev")  # .concat()
print(beatles)

beatles.extend(("Luke", "Kevin"))
print(beatles)

beatles.insert(0, "Middlesbrough")
print(beatles)

# Read
print(beatles[0])
print(beatles.pop(0))
print(beatles)

# Update
beatles[0] = "Jake"
print(beatles)

# Delete
del beatles[4:]
print(beatles)

print("Kevin" in beatles)
print("Jake" in beatles)

for member in beatles:
  print(f"{member} is in the Beatles")


new_beatles = beatles.copy()
new_beatles.append("Luke")

print(new_beatles)
print(beatles)

beatles.sort(reverse=True)
print(beatles)

# DataFrame
# Series -> numpy arrays

bands = [[
  ["John", "Paul", "George", "Ringo"],
  ["Harry", "Liam", "Niall", "Zayn", "Louis"]
], [
  []
]]

print(bands[0][1][2])