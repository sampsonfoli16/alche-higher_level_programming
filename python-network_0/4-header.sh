#!/bin/bash
# Script that sends a GET request with a header variable and displays the body
url="$1"; [[ $url =~ ^https?:// ]] || url="http://$url"; curl -s -H "X-HolbertonSchool-User-Id: 98" "$url"
