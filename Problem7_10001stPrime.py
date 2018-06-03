import numpy as np

# first we can make use of the Sieve of Eratosthenes
# we will do this by making a binary array
range = 1000000
myArray = np.ones((range,), dtype=int)

myArray[0] = 0
myArray[1] = 0

count1 = 2
count2 = 4

# creating the array
while count1 < range:
    if myArray[count1] == 1:
        while count2 < range:
            myArray[count2] = 0
            count2 += count1
    count1 += 1
    count2 = count1 * 2

# we can iterate through the array and count the 1's until we get to the
# 10001st 1
count = 0
numOnes = 0

while numOnes != 10001:
    if myArray[count] == 1:
        numOnes += 1

    count += 1

print(count-1)
