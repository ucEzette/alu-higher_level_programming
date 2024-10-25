#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        for i, element in enumerate(row):
            # Print element with str.format(), and avoid trailing space at the end of each row
            print("{:d}".format(element), end=" " if i < len(row) - 1 else "")
        print()  # Move to the next line after each row
