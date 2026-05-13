file = open("10_files/test.txt")

print(file.read())

file.close()

# context handler
with open("10_files/write.txt", mode="a", newline="") as file:
  file.write("Hello\n")
  file.write("Python is great!\n")
  file.write("Is the summer over already?\n")




