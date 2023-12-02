#!/usr/bin/python3
"""sends a POST request to http://0.0.0.0:5000/search_user"""
if __name__ == "__main__":
    import requests
    import sys
    url = "http://0.0.0.0:5000/search_user"
    if len(sys.argv) > 1:
        q = sys.argv[1]
    else:
        q = ""
    query = {'q': q}
    response = requests.post(url, data=query)
    if response.status_code != requests.codes.ok or len(response.text) <= 0:
        print('No result')
        sys.exit()
    else:
        try:
            attrib = response.json()
            if len(attrib) == 0:
                print('No result')
                sys.exit()
            response_id = attrib.get('id')
            response_name = attrib.get('name')
            print("[{}] {}".format(response_id, response_name))
        except ValueError as invalid_json:
            print('Not a valid JSON')
