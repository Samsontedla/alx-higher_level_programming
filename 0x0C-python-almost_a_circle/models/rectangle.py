#!/usr/bin/python3
"""
File: rectangle.py

Author: Samson Tedla <samitedla23@gmail.com>

Class that defines a rectangle
"""
from models.base import Base


class Rectangle(Base):
    """
    A class that represents a rectangle
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialize a new Rectangle

        Args:
            width (int): width of rectangle
            height (int): height of rectangle
            x (int): the x coordinate of the rectangle
            y (int): the y coordinate of the rectangle
            id (int): the idnentity of the rectangle
        Rasies:
            TypeError: If either of width or height is not an int.
            ValueError: If either of width or height <= 0.
            TypeError: If either of x or y is not an int.
            ValueError: If either of x or y < 0.
        """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """Get/set width of a rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """Get/set height of a rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """Get/set x coordinate of a rectangle"""
        return self.__x

    @x.setter
    def x(self, value):
        if type(value) != int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """Get/set y coordinate of a rectangle"""
        return self.__y

    @y.setter
    def y(self, value):
        if type(value) != int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        "method that returns area of the rectangle"""
        return self.__width * self.__height
