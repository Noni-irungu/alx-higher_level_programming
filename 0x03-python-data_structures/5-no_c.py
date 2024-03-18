#!/usr/bin/python3

'''A function that removes certain
characters'''


def no_c(my_string):
    updated_string = ""
    for elements in my_string:
        if elements != "c" and elements != "C":
            updated_string += elements
        return updated_string
