#!/usr/bin/python3

'''A function that replaces an element of a list'''


def replace_in_list(my_list, idx, element):
    if idx < 0:
        return my_list
    elif idx >= len(my_list):
        return mylist
    else:
        my_list[idx] = element
        return my_list
