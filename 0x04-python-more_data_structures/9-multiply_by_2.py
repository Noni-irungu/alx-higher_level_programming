#!/usr/bin/python3

'''A function that returns a new dictionary with
its values multiplied by 2'''


def multiply_by_2(a_dictionary):
    return {key: num*2 for key, num in a_dictionary.items()}
