#!/usr/bin/python3
"""
Module containing inherits_from function
"""


def inherits_from(obj, a_class):
    """
    returns True if the object is an instance of a class that inherited
    (directly or indirectly) from the specified class ; otherwise False.
    :param obj:  object to test
    :param a_class: class to test over
    :return: True or false on each case.
    """
    return issubclass(type(obj), a_class) and type(obj) is not a_class
