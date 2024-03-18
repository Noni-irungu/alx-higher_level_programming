#!/usr/bin/python3

'''A function that prints a matrix of integers'''


def print_matrx_integer(matrix=[[]]):
    for row in matrix:
        for column in row:
            if column != row[-1]:
                print("{:d}".format(column), end=" ")
            else:
                ""
        print()
