# We need to get the largest palindrome of the product of two 3 digit numbers

num1 = 999
num2 = 999
tot = num1 * num2
largestPalindrome = 0


def checkPalindrome(num):
    temp = num
    reverseNum = 0

    while temp != 0:
        digit = temp % 10  # get the end digit
        reverseNum = (reverseNum * 10) + digit  # put it into a new number
        temp = temp//10

    if num == reverseNum:
        return(num)
    else:
        return(-1)


while num1 > 1:
    while num2 > 1:
        tempPal = checkPalindrome(tot)
        if tempPal >= largestPalindrome:
            largestPalindrome = tempPal

        num2 = num2 - 1

        tot = num1 * num2
    num1 = num1 - 1
    num2 = num1

print(largestPalindrome)
