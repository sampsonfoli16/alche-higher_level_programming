#!/usr/bin/python3
"""Module that defines a read_file function."""


def read_file(filename=""):
    """Read a text file and print it to stdout."""
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
