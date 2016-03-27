"""
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.

ANSWER: 142913828922
"""
import math


def is_prime(number):
    if number > 2 and number % 2 == 0:
        return False
    for i in range(3, int(math.sqrt(number)) + 1, 2):
        if number % i == 0:
            return False
    return True

answer = 2 + sum([x for x in xrange(3, 2000001, 2) if is_prime(x)])

print "ANSWER: " + str(answer)
