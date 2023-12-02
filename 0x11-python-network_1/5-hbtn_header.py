#!/usr/bin/python3
"""sends a request to the URL and displays the value variable X-Request-Id"""
if __name__ == "__main__":
    import urllib.requests
    import sys
    url = sys.argv[1]
    with urllib.request.urlopen(url) as response:
        inhead = response.info()
        for header in inhead._headers:
            if header[0] == 'X-Request-Id':
                print(header[1])
