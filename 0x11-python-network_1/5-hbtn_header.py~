#!/usr/bin/python3
"""script that takes in a URL, sends a request to the URL"""
if __name__ == "__main__":
    import urllib.request
    import sys
    url = sys.argv[1]
    with urllib.request.urlopen(url) as response:
        inhead = response.info()
        for header in inhead._headers:
            if header[0] == 'X-Request-Id':
                print(header[1])
