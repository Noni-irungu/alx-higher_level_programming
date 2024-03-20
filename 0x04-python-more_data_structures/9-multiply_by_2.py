#!/usr/bin/python3

'''A function that returns a new dictionary with
its values multiplied by 2'''


def multiply_by_2(a_dictionary):
    nw_dicti = {}
    for j in a_dictionary:
        nw_dicti[j] = a_dictionary[j] * 2
    return nw_dicti
