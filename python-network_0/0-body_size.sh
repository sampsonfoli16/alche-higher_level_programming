#!/bin/bash
# Script that takes a URL, sends a request and displays the size of the body in bytes
url="$1"; [[ $url =~ ^https?:// ]] || url="http://$url"; curl -s "$url" | wc -c
