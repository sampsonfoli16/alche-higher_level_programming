#!/usr/bin/python3
"""Module that defines a lookup function."""


def lookup(obj):
    """Return list of available attributes and methods of an object."""
    return dir(obj)
