#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)

num = repr(number)

last = num[-1]

last = int(last)

if (number > 0) and (last > 5):
    print(f"Last digit of {number:d} is {last:d} and is greater than 5")

elif (last == 0):
    print(f"Last digit of {number:d} is {last:d} and is 0")

elif (number < 0) and (last != 0):
    print(f"Last digit of {number:d} is -{last:d} and is less than 6 and not 0")

else:
    print(f"Last digit of {number:d} is {last:d} and is less than 6 and not 0")
