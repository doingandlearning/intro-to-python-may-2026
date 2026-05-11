print("My favourite number is " + str(42))
print(f"My favourite number is {42}")

#                    
#      0123456789 
print("This is a long string"[0:10:2])  # [start:end:step]
print("This is a long string"[:-4])  # [start:end:step]
print("This is a long string"[-3:])  # [start:end:step]

print("%s is my name".format("Kevin"))

print(round(1.831231231, 4))

print(12//5)
print(12/5)

hour = 11

print(f"The time in 27 hours will be {(11 + 27) % 24}")
print(f"{3 % 2}")
print(f"{4 % 2}")

print(5 ** 3)

print(str(23))
# print(int("twenty four"))

user_number = input("Give me a number: ")

print(f"One more than your number is {int(user_number) + 1}")

print("1" + "1")