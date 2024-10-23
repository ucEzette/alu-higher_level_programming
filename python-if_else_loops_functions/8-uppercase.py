def uppercase(str):
    for c in str:
        if ord(c) >= 97 and ord(c) <= 122:  # Check if the character is lowercase
            c = chr(ord(c) - 32)  # Convert to uppercase by subtracting 32 from the ASCII value
        print("{}".format(c), end="")
    print()  # Print a new line at the end
