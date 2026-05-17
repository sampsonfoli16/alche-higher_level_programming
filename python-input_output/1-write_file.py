#!/usr/bin/python3
"""Module that defines a write_file function."""


def write_file(filename="", text=""):
    """Write a string to a text file and return number of characters."""
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
