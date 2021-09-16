#!/usr/bin/pyhton3


def print_sorted_dictionary(a_dictionary):
    '''function that prints a dictionary by ordered keys'''
    for i, j in sorted(a_dictionary.items()):
        print("{}: {}".format(i, j))
