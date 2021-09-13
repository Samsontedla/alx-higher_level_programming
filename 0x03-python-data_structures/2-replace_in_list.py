#!/usr/bin/python3
'''function that replaces an element of a list at a specific position'''


def replace_in_list(my_list, idx, element):
    for i in range(0, len(my_list)):
        if i == idx:
            my_list[i] = element
