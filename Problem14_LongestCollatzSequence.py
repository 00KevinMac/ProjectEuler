# Find the longest chain with a starting number under 1 million

startingNum = 999999
finalNum = 0
counter = 1
maxCount = 0

for i in range(1, 1000000):

    startingNum = i

    while i != 1:
        if i % 2 == 0:  # even
            i = i/2
        else:
            i = 3*i + 1

        counter += 1

    if counter > maxCount:
        maxCount = counter
        finalNum = startingNum

    counter = 1

print(finalNum)