#!/usr/bin/python3


class Rectangle:
    """A Class for building a rectangle"""

    def __init__(self, width=0, height=0):
        """inititalizes the rectabngle"""
        self.width = width
        self.height = height

    @property
    def width(self):
        """Getter for for private instance attribute widght"""
        return self.__width

    @width.setter
    def width(self, value):
        """Setter for private instance attribute width"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Getter for private instance attribute height"""
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__height = value
