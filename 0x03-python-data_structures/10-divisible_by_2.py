#!/usr/bin/python3

'''A function that finds all multiples of 2
in a list'''


def divisible_by_2(my_list=[]):
    update_list = []
    for k in range(len(my_list)):
        if my_list[k] % 2 == 0:
            updated_list.append(True)
        else:
            updated_list.append(False)
    return updated_list
