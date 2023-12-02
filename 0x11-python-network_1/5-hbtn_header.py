#!/usr/bin/python3
"""sends a request to the URL and displays the value variable X-Request-Id"""
if __name__ == "__main__":
    import requests
    import sys
    url = sys.argv[1]
    response = requests.get(url)
    inhead = response.headers
    print(inhead.get('X-Request-Id'))
