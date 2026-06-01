#!/bin/bash
# Script that sends a POST request with email and subject parameters
url="$1"; [[ $url =~ ^https?:// ]] || url="http://$url"; curl -s -X POST -d "email=test@gmail.com&subject=I will always be here for PLD" "$url"
