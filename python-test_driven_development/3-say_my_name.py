#!/usr/bin/python3
"""Print "My name is <first_name> <last_name>" after validation.

Function `say_my_name(first_name, last_name="")` validates parameters are
strings and prints the formatted name.
"""


def say_my_name(first_name, last_name=""):
    """Print the full name after validating parameter types.

    Raises TypeError with specific messages when types are invalid.
    """
    if not isinstance(first_name, str):
        raise TypeError('first_name must be a string')
    if not isinstance(last_name, str):
        raise TypeError('last_name must be a string')

    if last_name == "":
        print("My name is {}".format(first_name))
    else:
        print("My name is {} {}".format(first_name, last_name))
