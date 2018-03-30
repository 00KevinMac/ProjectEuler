# We need to find the sum of all numbers divisible by 3 and by 5 up to 1000

sum = 0

for x in range(3, 1000):
    if x % 3 == 0 or x % 5 == 0:
        sum += x

print(sum)
