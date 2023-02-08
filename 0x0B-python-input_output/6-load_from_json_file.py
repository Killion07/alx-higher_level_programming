#!/usr/bin/python3
"""
function for creating an object
"""

import json


def load_from_json_file(filename):
    """crates an object"""
    with open(filename, 'r', encoding='utf-8') as f:
        return json.load(f)
