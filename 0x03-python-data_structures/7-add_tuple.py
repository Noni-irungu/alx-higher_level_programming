#!/usr/bin/python3

'''A function that adds 2 tuples'''


def add_tuple(tuple_a=(), tuple_b=()):
    tuple_1 = tuple_a[0]
    if len(tuple_a) > 0:
        print(tuple_1)
    else:
        print(0)
    tuple_2 = tuple_a[1]
    if len(tuple_a) > 0:
        print(tuple_2)
    else:
        print(0)
    tuple_1_b = tuple_b[0]
    if len(tuple_b) > 0:
        print(tuple_1_b)
    else:
        print(0)
    tuple_2_b = tuple_b[1]
    if len(tuple_b) > 0:
        print(tuple_2_b)
    else:
        print(0)

    sum_1 = tuple_1 + tuple_1_b
    sum_2 = tuple_2 + tuple_2_b

    return (sum_1, sum_2)
