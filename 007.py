"""
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?

ANSWER: 104743
"""

import math


def is_prime(number):
    if number > 2 and number % 2 == 0:
        return False
    for i in range(3, int(math.sqrt(number)) + 1, 2):
        if number % i == 0:
            return False
    return True


counter = 1
x = 1
while counter < 10001:
    x += 2
    if is_prime(x):
        counter += 1


print "ANSWER: " + str(x)
