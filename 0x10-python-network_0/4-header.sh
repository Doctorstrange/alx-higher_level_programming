#!/bin/bash
# takes in a URL as an argument, sends a GET request
curl -s -H "X-HolbertonSchool-User-Id: 98" "$1"
