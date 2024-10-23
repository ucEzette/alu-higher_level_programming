#!/usr/bin/python3
for ascii_char in range(97, 123):
    if ascii_char != 101 and ascii_char != 113:
        print("{}".format(chr(ascii_char)), end=" ")
