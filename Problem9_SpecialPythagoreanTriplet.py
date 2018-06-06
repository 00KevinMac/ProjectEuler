# we need to find the product of the pythagorean triplet a, b, c that
# adds up to 1000

a = 1
b = 1
c = 998
found = False

while a < 1000 and found is False:
    for x in range(1, 1000):
        b = x
        c = 1000 - a - x
        if (a * a + b * b) == c * c:
            print(a*b*c)
            found = True
            break

    a += 1
