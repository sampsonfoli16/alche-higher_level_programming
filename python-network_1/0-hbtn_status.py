#!/usr/bin/python3
"""Fetches the status from the Holberton intranet API."""

from urllib import request

if __name__ == "__main__":
    url = 'https://alu-intranet.hbtn.io/status'
    with request.urlopen(url) as response:
        content = response.read()
        print('Body response:')
        print('\t- type:')
        print('\t- content: {}'.format(content))
        print('\t- utf8 content: {}'.format(content.decode('utf-8')))
