#!/usr/bin/python3

'''A function that prints all integers'''


def print_list_integer(my_list=[]):
    for i in range(len(my_list)):
        print("{:d}".format(my_list[i]))
