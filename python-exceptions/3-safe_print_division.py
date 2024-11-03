#!/usr/bin/python3
def safe_print_division(a, b):
    result = None  # Initialize result to None
    try:
        result = a / b  # Attempt to divide a by b
    except ZeroDivisionError:
        result = None  # Set result to None if division by zero occurs
    finally:
        print("Inside result: {}".format(result))  # Print result in the finally block
    return result  # Return the result of the division or None
