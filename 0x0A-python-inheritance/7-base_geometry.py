#!/usr/bin/python3
"""
Module containing BaseGeometry class
"""


class BaseGeometry:
    """
    BaseGeometry class.
    """

    def area(self):
        """
        Area method.

        Raises:
            Exception: If area() is not implemented.

        Returns:
            None
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Integer validator method.

        Args:
            name (str): The name of the value.
            value (int): The value to validate.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than or equal to zero.

        Returns:
            None
        """
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
