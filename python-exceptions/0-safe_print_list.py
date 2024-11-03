def safe_print_list(my_list=[], x=0):
    count = 0  # To keep track of the number of elements printed
    try:
        for i in range(x):
            print(my_list[i], end='')  # Print each element on the same line
            count += 1
    except IndexError:
        pass  # Stop printing if we go beyond the list's length
    print()  # Move to a new line after printing elements
    return count  # Return the actual number of elements printed
