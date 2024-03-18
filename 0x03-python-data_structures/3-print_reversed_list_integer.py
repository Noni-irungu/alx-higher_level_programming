#!/usr/bin/python3

'''A function that prints all integers
in reverse'''


def print_reversed_list_integer(my_list=[]):
    if my_list:
        for i in range(len(my_list)):
            print("{:d}".format(my_list[i].reverse()))
