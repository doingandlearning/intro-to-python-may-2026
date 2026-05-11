my_favourite_number = 42  # int -> integer -> whole number
print(my_favourite_number)
print(type(my_favourite_number))

my_favourite_number = 42.5  # float -> floating point number - decimal
print(my_favourite_number)
print(type(my_favourite_number))

my_favourite_number  # double underscore -> dunders

##                     012345678
my_favourite_number = "forty two"  # str -> string 
print(my_favourite_number)
print(type(my_favourite_number))
print(my_favourite_number.capitalize())
print(my_favourite_number.upper())

print("hello   ".upper().strip() == "HELLO")

print(my_favourite_number.find("two"))
print(my_favourite_number.find("kevin"))
print(my_favourite_number.replace("two", "three"))

print(my_favourite_number.replace(" ", "_").lower())

my_favourite_number = "forty two"
my_favourite_number = 'forty two'
my_favourite_number = "This isn't on!"
my_favourite_number = '''3 Street
This City
This Country'''

first_name = "Luke"
last_name = "Symmonds"
location = "Middlesbrough"

# concatenation
greeting = first_name + " "  + last_name + " lives in " + location + ", say hello!"
greeting = f"{first_name.upper()} {last_name} lives in {location}, say hello!"
print(greeting)

print(f"1 + 1 = {1+1}")
