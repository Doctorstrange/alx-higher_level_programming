#!/usr/bin/python3
for ascval in range(97, 123):
    if chr(ascval) not in ['q', 'e']:
        print("{}".format(chr(ascval)), end="")
