#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    count = 0  # Counter for the number of integers printed
    for i in range(x):
        try:
            print("{:d}".format(my_list[i]), end='')  # Attempt to print as integer
            count += 1  # Increment count if successful
        except (ValueError, TypeError):
            continue  # Skip non-integer values
        except IndexError:
            break  # Stop if x is greater than the list length
    print()  # Move to a new line after printing all integers
    return count  # Return the count of integers printed
