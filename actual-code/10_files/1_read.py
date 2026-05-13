# <_io.TextIOWrapper name='10_files/test.txt' mode='r' encoding='UTF-8'>
# \n   - UTF-8
# \n\r - CP-65001

file = open("10_files/test.txt", newline="")

# read()
contents = file.read() # str of the file
print(contents)
print(type(contents))

print("Glass" in contents)

# readlines()
file.seek(0) # move the cursor to the start of the file
contents = file.readlines()  # a list of the file, one element for line
print(contents)
print(type(contents))

for thing in contents:
  print(thing.strip())

# readline()
file.seek(0)
line = file.readline()
while line:
  print(line.strip())
  line = file.readline()

print("=" * 10)
file.seek(0)
for line in file:
  print(line.strip())


file.close()