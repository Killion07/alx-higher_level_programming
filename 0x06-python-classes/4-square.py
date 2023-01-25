#!/usr/bin/python3
"""Define a class"""


class Square:
    """initialize the attributes"""

    def __init__(self, size=0):
        """Initialize the square
        """
        self.size = size

    def area(self):
        """Returns the area of the square"""

        return (self.__size) ** 2

    @property
    """Geeter of size and returns size"""
    def size(self):
        return self.__size

    @setter
    def size(self, value):
        """Checks and sets the size"""
        if type(value) is not int:
            raise TypeError("size must be an integer")
        else:
            if value < 0:
                raise ValueError("size must be >= 0")
            else:
                self.__size = value
