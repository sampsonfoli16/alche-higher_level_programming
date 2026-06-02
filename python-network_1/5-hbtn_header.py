#!/usr/bin/python3
"""Displays the X-Request-Id header value for a given URL using requests."""

import requests
import sys


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: ./5-hbtn_header.py <URL>", file=sys.stderr)
        sys.exit(1)

    url = sys.argv[1]
    response = requests.get(url)
    print(response.headers.get('X-Request-Id'))
