#!/usr/bin/python3

'''A function that computes the square value of
all integers of a matrix using map'''


def square_matrix_map(matrix=[]):
    return list(map(lambda row: list(map(lambda colu: colu**2, row)), matrix))
