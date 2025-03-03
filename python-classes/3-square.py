#!/usr/bin/python3
# Define a class 'Square' with private instance attribute 'size'
"""
    Define a class 'Square' that defines a square.
"""


class Square:
    """
    Square class defines a square with private size attribute
    """

    def __init__(self, size=0):
        """
        Initialize the square with size
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size

    def area(self):
        """
        Return the current area of the square.
        """
        return self.__size ** 2
