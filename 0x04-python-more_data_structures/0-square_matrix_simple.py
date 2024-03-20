#!/usr/bin/python3

'''A function that computes the square value
of all integers of a matrix'''


def square_matrix_simple(matrix=[]):
    sqr_mtrx = [[t ** 2 for t in row] for row in matrix]
    return sqr_mtrx
