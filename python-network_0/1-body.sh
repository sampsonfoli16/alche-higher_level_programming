#!/bin/bash
# Script that sends a GET request and displays the body of a 200 status code response
[ "$(curl -s -o /dev/null -w '%{http_code}' "$1")" = "200" ] && curl -s "$1"
