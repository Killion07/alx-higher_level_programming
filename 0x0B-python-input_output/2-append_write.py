#!/usr/bin/python3
"""
Function append_write for appening text
"""


def append_write(filename="", text=""):
    """Used to append text on an file that's existing"""
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
