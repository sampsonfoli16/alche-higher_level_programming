#!/usr/bin/python3
"""Fetches https://intranet.hbtn.io/status."""
import requests


if __name__ == "__main__":
    # Some test environments may present SSL issues for the external URL.
    # Disable verification and suppress the related warning to ensure
    # the script can fetch the content in those environments.
    try:
        from requests.packages.urllib3.exceptions import InsecureRequestWarning
        requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
    except Exception:
        pass

    r = requests.get("https://intranet.hbtn.io/status", verify=False)
    print("Body response:")
    print("\t- type: {}".format(type(r.text)))
    print("\t- content: {}".format(r.text.strip()))
