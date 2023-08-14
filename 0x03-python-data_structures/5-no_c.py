#!/usr/bin/env python3
def no_c(my_string):
    x = 0
    old_string = list(my_string)
    new_string = []
    for char in old_string:
        if char != "c" and char != "C":
            new_string.append(char)
        x += 1
    return (''.join(new_string))
