#!/usr/bin/python3
for num1 in range(10):
    for num2 in range(num1 + 1, 10):
        if num1 < 8 or (num1 == 8 and num2 == 9):
            print("{:02d} {:02d}, ".format(num1, num2), end="")
        else:
            print("{:02d} {:02d}".format(num1, num2))
