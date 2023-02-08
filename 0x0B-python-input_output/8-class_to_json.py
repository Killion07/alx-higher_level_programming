#!/usr/bin/python3
"""
class to json function
"""


def class_to_json(obj):
    """Returns dictionary description"""
    return obj.__dict__
