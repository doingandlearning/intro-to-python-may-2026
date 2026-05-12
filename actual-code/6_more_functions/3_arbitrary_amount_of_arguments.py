def add(a, b, c=0, d=0):
  return a + b + c + d

print(add(1,2))
print(add(1,2,3))
print(add(1,2,3,4))

def other_add(*nums):
  total = 0
  for number in nums:
    total = total + number
  return total

print(other_add(1,2))
print(other_add(1,2,3))
print(other_add(1,2,3,4))
print(other_add(1))
print(other_add())
print(other_add(1,2,3,4,5,6,7,12,12,123,123,12,124,14,14,14))

# *args
def join_spreadsheets(*sheets):
  pass

def custom_print(name, *things_to_print):
  print(f"This has been printed by {name}")
  print(*things_to_print)

custom_print("Kevin", "Hello", "How are you?", "What's going on?")