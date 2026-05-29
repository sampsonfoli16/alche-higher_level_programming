#!/bin/bash
# Script that takes a URL, sends a request and displays the size of the body in bytes
curl -s -o /dev/null -w '%{size_download}' "$1"
