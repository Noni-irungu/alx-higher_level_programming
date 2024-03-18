#!/usr/bin/python3

'''A function that adds 2 tuples'''


def add_tuple(tuple_a=(), tuple_b=()):
    summation_tuple = ()
    tuple_a_1 = tuple_a + (0, 0)
    tuple_b_2 = tuple_b + (0, 0)
    summation_tuple = tuple_a_1[0] + tuple_b_2[0], tuple_a_1[1] + tuple_b_2[1]
    return (summation_tuple)
