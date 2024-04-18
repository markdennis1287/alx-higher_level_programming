#!/usr/bin/python3
"""
Module containing MyInt class
"""


class MyInt(int):
    """
    MyInt class.
    """

    def __eq__(self, other):
        """
        eq method for equality
        :param other: the attribute
        :return: ne method for inequality
        """
        return super().__ne__(other)

    def __ne__(self, other):
        """
        ne method for inequality
        :param other: attribute
        :return: eq method for equality
        """
        return super().__eq__(other)
