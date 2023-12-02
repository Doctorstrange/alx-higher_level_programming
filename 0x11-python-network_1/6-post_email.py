#!/usr/bin/python3
"""takes in a URL and an email address, sends a POST request to passed URL"""
if __name__ == "__main__":
    import requests
    import sys
    url = sys.argv[1]
    email = sys.argv[2]
    packet = {'email': email}
    response = requests.post(url, data=packet)
    print(response.text)
