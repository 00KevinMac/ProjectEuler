# We need to find the sum of even valued fibonacci numbers, up to four million

num1 = 1
num2 = 1
fibNum = 0
sum = 0

while fibNum < 4000000:
    fibNum = num1 + num2
    num1 = num2
    num2 = fibNum
    if fibNum % 2 == 0:
        sum += fibNum

print(sum)
