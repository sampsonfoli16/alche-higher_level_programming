#!/usr/bin/python3
"""Displays the X-Request-Id header variable of a request to a given URL.

Usage: ./1-hbtn_header.py <URL>
"""
import sys
import urllib.request
import urllib.error


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: ./1-hbtn_header.py <URL>", file=sys.stderr)
        sys.exit(1)

    url = sys.argv[1]
    request = urllib.request.Request(url)
    try:
        with urllib.request.urlopen(request) as response:
            # Use getheader to retrieve a single header value
            print(response.getheader("X-Request-Id"))
    except urllib.error.HTTPError as err:
        print(err, file=sys.stderr)
    except urllib.error.URLError as err:
        print(err, file=sys.stderr)
