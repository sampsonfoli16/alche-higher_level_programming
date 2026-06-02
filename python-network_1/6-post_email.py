#!/usr/bin/python3
"""Sends an email address in a POST request and displays the response."""

import requests
import sys


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: ./6-post_email.py <URL> <email>", file=sys.stderr)
        sys.exit(1)

    url = sys.argv[1]
    email = sys.argv[2]
    response = requests.post(url, data={'email': email})
    print(response.text)
