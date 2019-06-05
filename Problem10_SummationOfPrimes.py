# We need to find the sum of all primes under 2 million

import numpy as np

length = 2000000


# creates the Sieve of Eratosthenes
def create_sieve(rng):
    myArray = np.ones((rng,), dtype=int)

    myArray[0] = 0
    myArray[1] = 0

    count1 = 2
    count2 = 4

    # creating the array
    while count1 < rng:
        if myArray[count1] == 1:
            while count2 < rng:
                myArray[count2] = 0
                count2 += count1
        count1 += 1
        count2 = count1 * 2

    return myArray


# adds together the prime numbers
def add_primes(primeArray):
    total = 0

    for x in range(len(primeArray)):
        if primeArray[x] == 1:
            total += x

    return total


sieveArray = create_sieve(length)
sumOfPrimes = add_primes(sieveArray)

print(sumOfPrimes)
