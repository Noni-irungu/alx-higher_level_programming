#!/usr/bin/python3

'''A function that removes certain
characters'''


def no_c(my_string):
    updated_string = my_string.translate({ord(i): None for i in 'cC'})
    return updated_string
