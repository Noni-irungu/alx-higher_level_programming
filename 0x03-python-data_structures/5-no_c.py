#!/usr/bin/python3

'''A function that removes certain
characters'''


def no_c(my_string):
    new_string = ""
    for elements in my_string:
        if elements != "c" and elements != "C":
            new_string += elements
        return new_string
