import numpy as np
import math

# We need to find the smallest number divisible by numbers 1-20
# We can multiply all the prime numbers together from 1-20

range = 21
smallestMult = 1

# We will use a seive of Eratosthenes
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

index = 0

# we can multiply the prime numbers together
while index < range:
    if myArray[index] == 1:
        smallestMult = smallestMult*index

    index = index + 1

index = 1

# Now we check if all numbers divide the number
while index < range:
    if smallestMult % index != 0:
        tempIndex = 2
        while tempIndex < index:
            if index % tempIndex == 0:
                smallestMult = smallestMult * tempIndex
                break

            tempIndex = tempIndex + 1

    index = index + 1

print(myArray)
print(smallestMult)
