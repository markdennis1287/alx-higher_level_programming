#!/usr/bin/python3
"""
Module containing lookup function
"""


def lookup(obj):
    """
    returns the list of available attributes and methods of an object
    :param obj: the object
    :return: list of available attributes and methods of the object
    """
    return dir(obj)
