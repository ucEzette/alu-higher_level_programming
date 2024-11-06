#!/usr/bin/python3
def safe_print_integer(value):
    try:
        print("{:d}".format(value))  # Attempt to format and print
        return True  # Return True if no error occurs
    except (ValueError, TypeError):
        return False  # Return False if formatting fails
