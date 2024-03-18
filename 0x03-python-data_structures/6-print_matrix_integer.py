#!/usr/bin/python3

'''A function that prints a matrix of integers'''


def print_matrx_integer(matrix=[[]]):
    for row in matrix:
        for k in range(len(row)):
            if k == len(row) -1:
                print("{:d}".format(row[k]), end="")
            else:
                print("{:d}".format(row[k]), end=" ")
        print()
