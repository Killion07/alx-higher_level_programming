#!/usr/bin/python3
"""
Locked class
"""


class LockedClass:
    """
    Prevents user from instantiating any other class appert from first_name
    """

    __slots__ = ["first_name"]
