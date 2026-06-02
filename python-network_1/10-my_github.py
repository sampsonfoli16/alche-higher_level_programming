#!/usr/bin/python3
"""Displays the GitHub user id using Basic Authentication."""

import requests
import sys

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: ./10-my_github.py <username> <password>", file=sys.stderr)
        sys.exit(1)

    username = sys.argv[1]
    password = sys.argv[2]
    response = requests.get(
        'https://api.github.com/user', auth=(username, password)
    )
    if response.ok:
        print(response.json().get('id'))
    else:
        print(None)
