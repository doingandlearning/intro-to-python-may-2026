# data consistency
empty_tuple = ()  # tuple()
empty_tuple = tuple()

print(empty_tuple)
print(type(empty_tuple))

port_tuple = ("LIV", "MID", "SOU", "MAN")  

# quintuple
# hextuple

# () {} []  
# immutable -> unchangeable


print(port_tuple[0])
print(port_tuple[0:2])
print(port_tuple[2:]) # slicing, 

print(len(port_tuple))

print("MID" in port_tuple) # checking for membership

for port in port_tuple:  # loop
  print(f"{port} is a port in England")

print(port_tuple.count("SOU"))
print(port_tuple.count("EDI"))

print(port_tuple.index("SOU"))

if "EDI" in port_tuple:  # defensive programming
  print(port_tuple.index("EDI"))


middlesbrough = (54.5762, 1.2348)

long = middlesbrough[0]
lat = middlesbrough[1]

# unpacking
long, lat = middlesbrough