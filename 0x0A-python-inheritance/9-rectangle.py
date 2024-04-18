#!/usr/bin/python3
"""
Module containing BaseGeometry class
"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    Rectangle class.
    """

    def __init__(self, width, height):
        """
        Instantiation with width and height
        :param width: width of Rectangle
        :param height: height of Rectangle
        """
        self.__width = 0
        self.__height = 0
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        return self.__width * self.__height
