#!/usr/bin/python3
"""Sends an email address in a POST request and displays the response."""

import sys
from urllib import parse, request

if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]
    data = parse.urlencode({'email': email}).encode('ascii')
    req = request.Request(url, data=data)
    with request.urlopen(req) as response:
        print(response.read().decode('utf-8'))
