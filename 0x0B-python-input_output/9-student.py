#!/usr/bin/python3
"""
Class Student
"""


class Student:
    """Class student representation"""
    def __init__(self, first_name, last_name, age):
        """inititalizes details of the student"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """returns dictionary representation of student"""
        return self.__dict__
