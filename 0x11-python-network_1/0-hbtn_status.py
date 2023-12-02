#!/usr/bin/python3
"""Python script that fetches https://alx-intranet.hbtn.io/status"""
if __name__ == "__main__":
    import urllib.request
    url = "https://alx-intranet.hbtn.io/status"
    with urllib.request.urlopen(url) as response:
        read_content = response.read()
        encode_content = read_content.decode('utf-8')
        print_str = '''Body response:
\t- type: {}
\t- content: {}
\t- utf8 content: {}'''.format(type(read_content),
                               read_content, encode_content)
        print(print_str)
