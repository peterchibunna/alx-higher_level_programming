#!/usr/bin/python3
BaseGeometry = __import__('7-base_geometry').BaseGeometry

"""
Module:
8-rectangle
"""


class Rectangle(BaseGeometry):
    """Rectangle class that inherits from `BaseGeometry`"""

    def __init__(self, width, height):
        """initialize a rectangle of width and height"""
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
