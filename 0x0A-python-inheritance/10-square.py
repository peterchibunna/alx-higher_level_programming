#!/usr/bin/python3
"""
module: 9-rectangle:
with class Square
"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Square class that inherits Rectangle"""

    def __init__(self, size):
        """Initialises the attributes: size"""

        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        """redefine a area method in the parent class"""

        return self.__size ** 2

    def __str__(self):
        """__str__ method for return the next string"""

        return "[Rectangle] {}/{}".format(self.__size, self.__size)
