#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last_digit = str(number)
last_digit = last_digit[-1]
if number < 0:
    last_digit = -(int(last_digit))
else:
    last_digit = int(last_digit)
string = f"Last digit of {number} is {last_digit}"
if last_digit == 0:
    print(f"{string} and is 0", end="\n")
elif last_digit > 5:
    print(f"{string} and is greater than 5", end="\n")
else:
    print(f"{string} and is less than 6 and not 0", end="\n")
