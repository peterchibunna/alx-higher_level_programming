#!/usr/bin/python3
"""
Module: 7-base_geometry
A BaseGeometry class
"""


class BaseGeometry:
    """
    A BaseGeometry class with area
    """

    def area(self):
        """
        definition to calculate area
        """
        raise Exception('area() is not implemented')

    def integer_validator(self, name, value):
        """
        Validate the value passed as integer
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0 and type(value) is int:
            raise ValueError("{} must be greater than 0".format(name))
