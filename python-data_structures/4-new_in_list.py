#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    # Make a copy of the original list
    new_list = my_list[:]

    # Check if the index is within the valid range
    if 0 <= idx < len(my_list):
        # Replace the element at the specified index
        new_list[idx] = element

    # Return the modified copy (or original copy if idx is out of range)
    return new_list
