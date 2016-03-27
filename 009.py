"""
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

a2 + b2 = c2
For example, 32 + 42 = 9 + 16 = 25 = 52.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.

Find the product abc.

ANSWER: 31875000
"""

answer = 0
for x in range(1, 1000):
    for y in range(x + 1, 1000):
        z = 1000 - x - y
        if (x * x) + (y * y) == (z * z):
            answer = x * y * z

print "ANSWER: " + str(answer)
