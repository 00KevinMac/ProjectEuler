# We need to find the sum of the digits resulting from 2^1000

import math

power = int(math.pow(2, 1000))

stringPower = str(power)
totalSum = 0

for x in stringPower:
    totalSum += int(x)

print(totalSum)