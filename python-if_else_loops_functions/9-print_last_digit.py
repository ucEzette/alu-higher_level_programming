def print_last_digit(number):
    last_digit = abs(number) % 10  # Get the last digit using modulus
    print(last_digit, end="")  # Print the last digit without a new line
    return last_digit  # Return the last digit
