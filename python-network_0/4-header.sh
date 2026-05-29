#!/bin/bash
# Script that sends a GET request with a header variable and displays the body
curl -s -H "X-HolbertonSchool-User-Id: 98" "$1"
