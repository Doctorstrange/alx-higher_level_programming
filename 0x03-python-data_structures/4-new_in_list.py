#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    old_list = my_list.copy()
    if idx < 0 or idx > (len(my_list) - 1):
        return (my_list)
    else:
        old_list[idx] = element
        return (old_list)
