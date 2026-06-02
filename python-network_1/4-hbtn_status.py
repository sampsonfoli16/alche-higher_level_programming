#!/usr/bin/python3
"""Fetches https://intranet.hbtn.io/status."""
import requests
import warnings


if __name__ == "__main__":
    warnings.filterwarnings("ignore", message="Unverified HTTPS request")
    r = requests.get("https://intranet.hbtn.io/status", verify=False)
    print("Body response:")
    print("\t- type: {}".format(type(r.text)))
    print("\t- content: {}".format(r.text.strip()))
