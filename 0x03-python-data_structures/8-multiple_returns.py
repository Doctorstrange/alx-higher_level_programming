#!/usr/bin/python3
def multiple_returns(sentence):
    the_list = list(sentence)
    if the_list == "":
        return (0, None)
    mul_tuple = (len(sentence), the_list[0])
    return (mul_tuple)
