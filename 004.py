"""
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers
is 9009 = 91 * 99.

Find the largest palindrome made from the product of two 3-digit numbers.

ANSWER: 906609
"""


def is_palindrome(number):
    string = str(number)
    return str(string) == str(string)[::-1]

answer = 0

for x in xrange(100, 999):
    for y in range(100, 999):
        product = x * y
        if is_palindrome(product):
            if product > answer:
                answer = product

print "ANSWER : " + str(answer)
