# We need to find the number of different paths moving right and down on a 20x20 grid

# Seeing as we can only move right and down, this can be broken into a permutation problem
# We can have exactly 20 R's and 20 D's (where R = right and D = down)
# We just need to find the number of different ways these can be arranged

#   get the factorial of the total number of available options (40 in this case)
#   for each letter, divide by the factorial of the number of repeats

import math

gridSize = 20

result = math.factorial(gridSize*2) / (math.factorial(gridSize) * math.factorial(gridSize))

print(result)
