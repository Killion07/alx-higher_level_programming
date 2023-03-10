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
    def size(self):
        """Getter of size"""
        return self.__size

    @size.setter
    def size(self, value):
        """Checks and sets the size"""
        if type(value) is not int:
            raise TypeError("size must be an integer")
        else:
            if value < 0:
                raise ValueError("size must be >= 0")
            else:
                self.__size = value

    def my_print(self):
        """Prints the square
        Returns None:
        """
        if self.__size == 0:
            print()
            return
        for i in range(self.__size):
            print("".join(["#" for j in range(self.__size)]))
