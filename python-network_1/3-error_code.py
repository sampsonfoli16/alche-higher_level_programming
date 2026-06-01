#!/usr/bin/python3
"""Sends a request to a given URL and displays the response body.

Usage: ./3-error_code.py <URL>
  - Handles HTTP errors.
"""
import sys
import urllib.error
import urllib.request


if __name__ == "__main__":
  if len(sys.argv) != 2:
    print("Usage: ./3-error_code.py <URL>", file=sys.stderr)
    sys.exit(1)

  url = sys.argv[1]
  request = urllib.request.Request(url)
  try:
    with urllib.request.urlopen(request) as response:
      # decode using utf-8 to support common responses
      print(response.read().decode("utf-8"))
  except urllib.error.HTTPError as e:
    print("Error code: {}".format(e.code))
  except urllib.error.URLError as e:
    print(e.reason, file=sys.stderr)
