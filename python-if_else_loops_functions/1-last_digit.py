#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)

last_digit = abs(number) % 10  # Get the last digit (positive value)
if number < 0:
    last_digit *= -1  # Keep the sign if the number is negative

print(f"Last digit of {number} is {last_digit}", end=" ")

if last_digit > 5:
    print("and is greater than 5")
elif last_digit == 0:
    print("and is 0")
else:  # last_digit is less than 6 and not 0
    print("and is less than 6 and not 0")

