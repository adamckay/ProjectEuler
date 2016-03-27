"""
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

ANSWER: 232792560
"""


def is_divisible(number):
    # We only have to check prime factors
    numbers_to_divide = [11, 13, 14, 16, 17, 18, 19, 20]
    for divisor in numbers_to_divide:
        if number % divisor != 0:
            return False
    else:
        return True

found = False
num = 2520
while not found:
    if is_divisible(num):
        print "ANSWER: " + str(num)
        found = True
    else:
        num += 20
