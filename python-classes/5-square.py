#!/usr/bin/python3
"""
Define a class 'Square' with private 'size' attribute and m.
"""


class Square:
    """
    class with private size attribute and metho
    """

    def __init__(self, size=0):
        """
        Initialize the square with optional size.
        """
        self.size = size

    @property
    def size(self):
        """
        Get the size of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Set the size of the square.
        Validate: must be an integer and >= 0.
        """
i        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """
        Return the area of the square.
        """
        return self.__size ** 2

    def my_print(self):
        """
        Print the square with '#' characters.
        If size is 0, print an empty line.
        """
        if self.__size == 0:
            print("")
        else:
            for _ in range(self.__size):
                print("#" * self.__size)

