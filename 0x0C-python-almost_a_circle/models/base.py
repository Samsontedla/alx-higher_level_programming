#!/usr/bin/python3
"""
File: base.py

Author: Samson Tedla <samitedla23@gmail.com>

Defines a class called Base
"""

class Base:
    __nb_objects = 0
    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
