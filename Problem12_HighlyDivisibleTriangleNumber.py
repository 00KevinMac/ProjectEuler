# We need to find the triangle number, then check the mod values to see how many are divisors

import math

triangleNumber = 0
counter = 1
numDivisors = 0

while numDivisors < 500:
    triangleNumber += counter
    counter += 1

    for i in range(1, int(math.sqrt(triangleNumber+1))):
        if triangleNumber % i == 0:
            numDivisors += 2

    # check if there are over 500 divisors
    if numDivisors < 500:
        numDivisors = 0

print(triangleNumber)
