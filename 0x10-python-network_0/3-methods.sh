#!/bin/bash
# Bash script that takes in a URL and displays all HTTP methods the server
curl -s -I -X OPTIONS "$1" | grep 'Allow:' | cut -f2- -d' '
