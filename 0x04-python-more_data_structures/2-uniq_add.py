#!/usr/bin/python3

'''A function that adds all unique integers in a list
(only once for each integer)'''


def uniq_add(my_list=[]):
    add_list = set(my_list)
    summ_ation = 0
    for d in add_list:
        summ_ation += d
    return summ_ation
