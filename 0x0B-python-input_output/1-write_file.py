#!/usr/bin/python3
"""
Function that writes texts
"""


def write_file(filename="", text=""):
    """Wites a text and prints it out"""
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
