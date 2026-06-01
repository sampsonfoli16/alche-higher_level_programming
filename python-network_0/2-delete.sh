#!/bin/bash
# Script that sends a DELETE request and displays the body of the response
url="$1"; [[ $url =~ ^https?:// ]] || url="http://$url"; curl -s -X DELETE "$url"
