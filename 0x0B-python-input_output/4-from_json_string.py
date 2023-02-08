#!/usr/bin/python3
"""
Contains json string function
"""

import json


def from_json_string(my_str):
    """returns an object represetedin json string"""
    return json.loads(my_str)
