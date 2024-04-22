#!/usr/bin/python3
"""
Module containing class Square
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """
    Square class
    """
    def __init__(self, size, x=0, y=0, id=None):
        """
        Initialize Square
        :param size: size
        :param x: x
        :param y: y
        :param id: id
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """
        size getter
        :return: getter
        """
        return self.width

    @size.setter
    def size(self, value):
        """
        size setter.
        :param value: value
        :return: getter to value
        """
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """
        Args.
        :param args: no keywords
        :param kwargs: keywords
        :return: nothing.
        """
        if args:
            attributes = ["id", "size", "x", "y"]
            for i, arg in enumerate(args):
                if i < len(attributes):
                    setattr(self, attributes[i], arg)
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """
        To dictionary.
        :return: Dictionary.
        """
        return {
            'size': self.width,
            'x': self.x,
            'y': self.y,
            'id': self.id
        }

    def __str__(self):
        """
        Str method
        :return: str
        """
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"
