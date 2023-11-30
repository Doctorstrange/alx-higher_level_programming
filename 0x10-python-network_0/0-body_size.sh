#!/bin/bash
# script to get content-size
curl -Is "$1" | grep -w 'Content-Length' | cut -f2 -d' '
