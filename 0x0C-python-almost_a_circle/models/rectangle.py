#!/usr/bin/python3
"""
Module containing Class Rectangle
"""
from models.base import Base


class Rectangle(Base):
    """
    Rectangle class
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Initiate Rectangle
        :param width: width
        :param height: height
        :param x: x
        :param y: y
        :param id: id
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """
        width getter
        :return: getter
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        width setter
        :param value: value
        :return: getter to value
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """
        height getter
        :return: getter
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        height setter
        :param value: value
        :return: getter to value
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """
        x getter
        :return: getter
        """
        return self.__x

    @x.setter
    def x(self, value):
        """
        x setter
        :param value: value
        :return: getter to value
        """
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """
        y getter
        :return: getter
        """
        return self.__y

    @y.setter
    def y(self, value):
        """
        y setter
        :param value: value
        :return: getter to value
        """
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """
        Area.
        :return: area.
        """
        return self.__width * self.__height

    def display(self):
        """
        Display.
        :return: nothing.
        """
        for _ in range(self.__y):
            print()
        for _ in range(self.__height):
            print(" " * self.__x + "#" * self.__width)

    def update(self, *args, **kwargs):
        """
        Update.
        :param args: args
        :param kwargs: kwargs
        :return: nothing.
        """
        attributes = ["id", "width", "height", "x", "y"]
        if args:
            for i, arg in enumerate(args):
                if i < len(attributes):
                    setattr(self, attributes[i], arg)
        elif kwargs:
            for key, value in kwargs.items():
                if key in attributes:
                    setattr(self, key, value)

    def to_dictionary(self):
        """
        To dictionary.
        :return: Dictionary.
        """
        return {
            'width': self.width,
            'height': self.height,
            'x': self.x,
            'y': self.y,
            'id': self.id
        }

    def __str__(self):
        """
        Str method.
        :return: str
        """
        return f"[Rectangle] ({self.id}) {self.x}/{self.y} - " \
               f"{self.width}/{self.height}"
