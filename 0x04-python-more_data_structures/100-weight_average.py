#!/usr/bin/python3

'''A function that returns the weighted average
of all integers tuple'''


def weight_average(my_list=[]):
    if my_list and len(my_list):
        nmrt = 0
        dnm = 0
        for tu_ple in my_list:
            nmrt += (tu_ple[0] * tu_ple[1])
            dnm += tu_ple[1]
        return (nmrt / dnm)
    return 0
