#!/usr/bin/python3

'''A function that finds the biggest integer
of a list'''


def max_integer(my_list=[]):
    if len(my_list) == 0:
        return 'None'
    else:
        max_num = my_list[0]
        for k in range(len(my_list)):
            if my_list[i] > max_num:
                max_num = my_list[i]
        return max_num
