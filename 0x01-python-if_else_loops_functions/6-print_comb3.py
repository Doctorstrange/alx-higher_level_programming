#!/usr/bin/python3
for value1 in range(0, 10):
    for value2 in range(value1 + 1, 10):
        if value1 == 8 and value2 == 9:
            print("{}{}".format(value1, value2))
        else:
            print("{}{}".format(value1, value2), end=", ")
