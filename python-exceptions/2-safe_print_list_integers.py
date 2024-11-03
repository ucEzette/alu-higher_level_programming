#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    count = 0  # Counter for the number of integers printed
    for i in range(x):
        try:
            print("{:d}".format(my_list[i]), end='')  # Attempt to print as integer
            count += 1  # Increment count if successful
        except (ValueError, TypeError):
            # Skip non-integer values without printing
            continue
        except IndexError:
            # Stop if x is greater than the list length
            break
    print()  # Move to a new line after printing all integers
    return count  # Return the count of integers printed
