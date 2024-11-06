#!/usr/bin/python3
# Define a class 'Square' with private instance attribute 'size'
"""
Define a class 'Square' with a private 'size' attribute
"""


class Square:
    """
    Class to define a square with a private 'size' attribute.
    """

    def __init__(self, size=0):
        """
        Initialize the square with optional size.
        """
        self.size = size

    @property
    def size(self):
        """
        Getter method for the size attribute.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Setter method for the size attribute.
        Validates the size to ensure it's an integer and >= 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """
        Return the current area of the square.
        """
        return self.__size ** 2
