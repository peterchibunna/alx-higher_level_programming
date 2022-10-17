#!/usr/bin/python3
"""
The Rectangle module

This module provides the Rectangle object
"""


class Rectangle(object):
    """ A Rectangle with attributes width and height """
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    def __str__(self):
        s = ""
        for y in range(self.height):
            s += ("#" * self.width) + "\n"
        return s

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError('width must be an integer')
        elif value < 0:
            raise ValueError('width must be >= 0')
        else:
            self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError('height must be an integer')
        elif value < 0:
            raise ValueError('height must be >= 0')
        else:
            self.__height = value

    def area(self):
        return self.width * self.height

    def perimeter(self):
        if self.width == 0 or self.height == 0:
            return 0
        return (self.width + self.height) * 2
