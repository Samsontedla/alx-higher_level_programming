#!/usr/bin/pyhton3


def square_matrix_simple(matrix=[]):
    '''function that computes the square value of all integers of a matrix'''
    square = [[y ** 2 for y in x] for x in matrix]
    return square
