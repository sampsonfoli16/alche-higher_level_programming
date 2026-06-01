#!/usr/bin/python3
"""Fetches the status from the Holberton intranet API."""

from urllib import error, request

if __name__ == "__main__":
    urls = [
        'https://intranet.hbtn.io/status',
        'https://alu-intranet.hbtn.io/status'
    ]
    for url in urls:
        try:
            with request.urlopen(url) as response:
                content = response.read()
                print('Body response:')
                print('\t- type:')
                print('\t- content: {}'.format(content))
                print('\t- utf8 content: {}'.format(content.decode('utf-8')))
                break
        except error.URLError:
            continue
