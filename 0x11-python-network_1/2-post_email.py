#!/usr/bin/python3
"""Python script that takes in a URL and an email, sends a POST"""
if __name__ == "__main__":
    import urllib.request
    import urllib.parse
    import sys
    url = sys.argv[1]
    email = sys.argv[2]
    inhead = {'email': email}
    inhead = urllib.parse.urlencode(inhead)
    inhead = inhead.encode('ascii')
    req = urllib.request.Request(url, inhead)
    with urllib.request.urlopen(req) as response:
        print(response.read().decode('utf-8'))
