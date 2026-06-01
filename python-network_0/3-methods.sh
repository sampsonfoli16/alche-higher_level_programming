#!/bin/bash
# Script that displays all HTTP methods the server will accept
url="$1"; [[ $url =~ ^https?:// ]] || url="http://$url"; curl -s -X OPTIONS "$url" -i | grep "Allow:" | cut -d' ' -f2-
