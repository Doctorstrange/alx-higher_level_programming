#!/usr/bin/python3
"""takes in a URL, sends a request to the URL and displays the body"""
if __name__ == "__main__":
    import requests
    import sys
    url = sys.argv[1]
    response = requests.get(url)
    if response.status_code != requests.codes.ok:
        print('Error code: {}'.format(response.status_code))
    else:
        print(response.text)
