#!/usr/bin/python3
# Define a class 'Square' with private instance attribute 'size'
"""
    Define a class 'Square' that defines a square.
"""

class Square:
    """
    Square class defines a square with private size attribute.
    """

    def __init__(self, size=0):
        """
        Initialize the square with size, with validation for integer and positive values.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        
        self.__size = size
