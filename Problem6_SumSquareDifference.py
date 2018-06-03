# We need the difference in the squareOfSums and the sumOfSquares

sumOfSquares = 0
squareOfSums = 0

for x in range(1, 101):
    sumOfSquares = sumOfSquares + x * x
    squareOfSums = squareOfSums + x

squareOfSums = squareOfSums * squareOfSums

print(squareOfSums - sumOfSquares)
