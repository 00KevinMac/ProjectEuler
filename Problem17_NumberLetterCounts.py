# We need to get the length of numbers written out in words

ones = ["", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", "eleven",
        "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]

twenties = ["", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]

def numToWord(num):
    unit = num % 10  # gets unit
    tens = ((num % 100) - unit) / 10  # gets tens (mod 100 gets the double digits leftover, then subtract the unit and divide by 10 to get the tens digit)
    hund = ((num % 1000) - (tens * 10) - unit) / 100

    numInWord = ""
    wordLength = 0

    if hund != 0 and tens == 0 and unit == 0:
        numInWord = ones[hund] + " hundred "
        wordLength = len(ones[hund]) + 7
    elif hund != 0:
        numInWord = ones[hund] + " hundred and "
        wordLength = len(ones[hund]) + 10

    if tens <= 1:
        numInWord += ones[num%100]
        wordLength += len(ones[num%100])
    elif tens > 1:
        numInWord += twenties[tens] + ones[unit]
        wordLength += len(twenties[tens]) + len(ones[unit])
    numInWord += str(wordLength)
    print(numInWord)
    return wordLength

totalLength = 0
for i in range(1, 1001):
    totalLength += numToWord(i)

# one thousand = 11 digits
totalLength += 11

print(totalLength)
