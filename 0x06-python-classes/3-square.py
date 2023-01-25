#!/usr/bin/python3
"""class square that calculates area"""


class Square:
    """Initializing the attributes"""

    def __init__(self, size=0):
        """
        Setting the arguments
        """

        if type(size) is int:
            if size < 0:
                raise ValueError('size must be >= 0')
            else:
                self.__size = size
        else:
            raise TypeError('size must be an integer')

    def area(self):
        """Finds and returns area
        """
        return self.__size * self__size
