#!/usr/bin/python3

'''A function that replaces a function
at a specific position'''


def new_in_list(my_list, idx, element):
    my_list_copy = my_list.copy()
    if idx < 0:
        return my_list_copy
    elif idx >= len(my_list):
        return my_list_copy
    else:
        my_list_copy[idx] = element
        return my_list_copy
