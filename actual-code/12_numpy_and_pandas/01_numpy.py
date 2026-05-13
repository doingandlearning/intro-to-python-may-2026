import numpy as np

# Numerical computing library

list_of_numbers = [1,2,3,4,5,6,7,8]
new_list = []
for value in list_of_numbers:
  new_list.append(value + 2)
list_of_numbers = new_list



np_array = np.array(list_of_numbers)
print(np_array)
# 1. Limits the datatype (saves memory)
# 2. Vectorize the calculations - 10-100x faster
np_array = np_array + 2
print(np_array)

zeros = np.zeros([2, 4])
print(zeros)

when_to_check = np.linspace(9, 17, 20)
print(when_to_check)

