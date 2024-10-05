import numpy as np

l = []
for i in range(1, 5):
    int_1 = int(input("Enter a number: "))  # Convert the input to an integer
    l.append(int_1)

print(np.array(l))  # This will now print a NumPy array of integers
