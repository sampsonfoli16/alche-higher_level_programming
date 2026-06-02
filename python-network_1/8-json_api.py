#!/usr/bin/python3
"""Searches for a user by letter using the provided API."""

import requests
import sys


if __name__ == "__main__":
    q = sys.argv[1] if len(sys.argv) > 1 else ""
    if q == "":
        print('No result')
        sys.exit(0)

    response = requests.get('http://0.0.0.0:5000/search_user', params={'q': q})
    try:
        data = response.json()
    except ValueError:
        print('Not a valid JSON')
    else:
        if data:
            print('[{}] {}'.format(data.get('id'), data.get('name')))
        else:
            print('No result')
