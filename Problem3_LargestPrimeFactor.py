import numpy as np
import math

# We need to find the largest prime number that evenly divides 600851475143
# We can check all the prime numbers up to the square root of that number
num = 600851475143
sqrtNum = round(math.sqrt(num))

# first we can make use of the Sieve of Eratosthenes
# we will do this by making a binary array
myArray = np.ones((sqrtNum,), dtype=int)

myArray[0] = 0
myArray[1] = 0

count1 = 2
count2 = 4

# creating the array
while count1 < sqrtNum:
    if myArray[count1] == 1:
        while count2 < sqrtNum:
            myArray[count2] = 0
            count2 += count1
    count1 += 1
    count2 = count1 * 2

# check if the number is divisible by any of the prime numbers
maxPrimaryNum = 1

for y in range(0, sqrtNum):
    if myArray[y] == 1:
        if num % y == 0:
            maxPrimaryNum = y

# if it isn't divisible by any prime numbers, then it must be a prime number
if maxPrimaryNum == 1:
    maxPrimaryNum = num

print(maxPrimaryNum)
