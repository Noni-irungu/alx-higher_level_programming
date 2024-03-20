#!/usr/bin/python3

'''A function that deletes keys with a specific
value in a dictionary'''


def complex_delete(a_dictionary, value):
    temp = a_dictionary.copy()
    for j, g in temp.items():
        if value == g:
            a_dictionary.pop(j)
    return a_dictionary
