#!/bin/bash
# Script that sends a GET request and displays the body of a 200 status code response
url="$1"; [[ $url =~ ^https?:// ]] || url="http://$url"; [ "$(curl -s -o /dev/null -w '%{http_code}' "$url")" = "200" ] && curl -s "$url"
