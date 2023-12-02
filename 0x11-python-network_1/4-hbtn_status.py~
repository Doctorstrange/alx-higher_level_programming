#!/usr/bin/python3
""""""
if __name__ == "__main__":
    import requests
    url = "https://alx-intranet.hbtn.io/status"
    packet = requests.get(url)
    content = packet.text
    printstr = '''Body response:
\t- type: {}
\t- content: {}'''.format(type(content), content)
    print(printstr)
