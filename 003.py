"""
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143?

ANSWER: 6857
"""

current_value = 2
largest = 600851475143L

while current_value < largest:
    if largest % current_value == 0:
        largest /= current_value
        current_value -= 1
    current_value += 1

print "ANSWER : " + str(current_value)
