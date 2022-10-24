#!/usr/bin/python3
"""A class: MyInt that inherits `int` type"""


class MyInt(int):
    """Invert int inbuilt operators == and !="""

    def __eq__(self, value):
        """Overwrite the `real` value of the int with the
        inverted operator"""
        return self.real != value

    def __ne__(self, value):
        """Overwrite the != operator with == operator"""
        return self.real == value
