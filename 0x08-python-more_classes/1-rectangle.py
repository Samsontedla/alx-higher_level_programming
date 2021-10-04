#!/usr/bin/python3
"""
File: 1-rectangle.py

Author: Samson Tedla <samitedla23@gmail.com>

Defines a class that represents a rectangle
"""


class Rectangle:
    """
    A class that defines a rectangle
    Args:
        width (int): width of rectangle
        height (int): height of rectangle
    Raises: 
        TypeError: if width/height is not integer
        ValueError: if width/height is < 0
    """
    def __init__(self, width=0, height=0):
        self.__width = width
        self.__height = height
    @property
    def width(self):
        return self.__width
    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value
    @property
    def height(self):
        return self.__height
    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
