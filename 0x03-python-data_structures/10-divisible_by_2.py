#!/usr/bin/python3

'''A function that finds all multiples of 2
in a list'''


def divisible_by_2(my_list=[]):
    update_list = []
    if my_list:
        for nums in my_list:
            updated_list.append(False if nums % 2 else True)
        return updated_list
