#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    bytwo = []
    for i in range(len(my_list)):
        if my_list[i] % 2 == 0:
            bytwo.append(True)
        else:
            bytwo.append(False)

    return (bytwo)
