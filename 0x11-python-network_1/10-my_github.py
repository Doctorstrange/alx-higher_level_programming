#!/usr/bin/python3
"""GitHub credentials (username and password) and uses the GitHub API"""
if __name__ == "__main__":
    import requests
    from requests.auth import HTTPBasicAuth
    import sys
    url = "https://api.github.com/"
    client_url = url + "client"
    username = sys.argv[1]
    password = sys.argv[2]
    response = requests.get(client_url,
                            auth=HTTPBasicAuth(username,
                                               password))
    if response.status_code == requests.codes.ok and len(response.text) > 0:
        try:
            attrib = response.json()
            print(attrib.get('id'))
        except ValueError as invalid_json:
            print('Not a valid JSON')
    else:
        print(None)
