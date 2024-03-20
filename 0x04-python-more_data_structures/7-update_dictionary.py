#!/usr/bin/python3

'''A function that replaces or add
key or value in a dictionary'''


def update_dictionary(a_dictionary, key, value):
    if key not in a_dictionary:
        a_dictionary[key] = value
    else:
        for k in a_dictionary:
            if k == key:
                a_dictionary[k] = value
    return a_dictionary
