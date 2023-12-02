#!/usr/bin/python3
"""takes 2 arguments in order to solve this challenge"""
if __name__ == "__main__":
    import requests
    import sys
    url = "https://api.github.com/"
    username = sys.argv[1]
    repo = sys.argv[2]
    push_url = url + "repos/{}/{}/commits".format(username, repo)
    response = requests.get(push_url)
    if response.status_code == requests.codes.ok and len(response.text) > 0:
        try:
            attrib = response.json()
            for x, att in enumerate(attrib):
                if x == 10:
                    break
                if type(att) is dict:
                    name = att.get('commit').get('author').get('name')
                    print("{}: {}".format(att.get('sha'), name))
        except ValueError as invalid_json:
            pass
