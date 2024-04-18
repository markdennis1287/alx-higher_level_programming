#!/usr/bin/python3
"""
Module containing Square class
"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    Square class.
    """

    def __init__(self, size):
        """
        Initializes size
        :param size: size of square
        """
        self.__size = 0
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def __str__(self):
        return "[Square] {}/{}".format(self.__size, self.__size)
