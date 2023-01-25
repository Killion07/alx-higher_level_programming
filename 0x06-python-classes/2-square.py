#!/usr/bin/python3
"""Creating a class for a square"""

class Square:
    """Initializing the size to zero"""
    def __init__(self, size = 0):
        self.__size = size
        try:
            size.isdigit()
        except TypeError:
            print("size must be an integer")
        try:
            size >= 0
        except ValueError:
            print("size must be >= 0")
