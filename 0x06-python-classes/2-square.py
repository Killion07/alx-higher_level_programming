#!/usr/bin/python3
"""Creating a class for a square"""


class Square:
    """Initializing the size to zero"""

    def __init__(self, size=0):
        """
        Args:
            size: size of square
        """

        if type(size) is int:
            if size < 0:
                raise ValueError('size must be >= 0')
            else:
                self.__size = size
        else:
            raise TypeError('size must be an integer')
