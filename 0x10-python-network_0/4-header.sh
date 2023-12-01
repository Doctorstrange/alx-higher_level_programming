#!/bin/bash
# url -s -X-HolbertonSchool-User-Id: 98" "$1"
curl -s -H "X-School-User-Id: 98" "$1"
