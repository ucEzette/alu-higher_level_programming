#!/usr/bin/python3
def safe_print_division(a, b):
    result = None  # Initialize result to None
    try:
        result = a / b  # Attempt to divide a by b
    except ZeroDivisionError:
        result = None
    finally:
        print("Inside result: {}".format(result))  # Print result
    return result
