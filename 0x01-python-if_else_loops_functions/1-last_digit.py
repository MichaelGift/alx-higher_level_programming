#!/usr/bin/python3
import random
num = random.randint(-10000, 10000)
if num < 0:
    first_digit = -num % 10
    last_digit = -last_digit
else:
    last_digit = num % 10
if last_digit > 5:
    print("Last digit of {} is {} and is greater
than 5".format(num, last_digit))
elif last_digit < 6 and last_digit != 0:
    print("Last digit of {} is {} and is less than 
6 and not 0".format(num, last_digit))
elif last_digit == 0:
    print("Last digit of {} is {} and is 0".format(num, last_digit))