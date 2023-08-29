#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    new_list = []
    for i in range(0, list_length):
        try:
            result = my_list_1[i] / my_list_2[i]
            if my_list_1[i] % my_list_2[i] != 0:
                new_list.append(0)
            else:
                new_list.append(result)
        except ZeroDivisionError:
            print("division by 0")
            new_list.append(0)
        except TypeError:
            print("wrong type")
            new_list.append(0)
        except IndexError:
            print("out of range")
            new_list.append(0)
    return new_list
