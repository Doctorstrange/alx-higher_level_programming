#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    count = (len(my_list) - 1)
    count = -count
    i = 0
    while i >= count:
        i = i + (-1)
        print("{}".format(my_list[i]))
