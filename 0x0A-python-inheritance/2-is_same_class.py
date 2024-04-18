#!/usr/bin/python3
"""
Module containing is_same_class function
"""


def is_same_class(obj, a_class):
    """
    returns True if the object is exactly an instance of the class
    :param obj: object to test
    :param a_class: class to test over
    :return: True if the object is exactly an instance of the class
    """
    return type(obj) is a_class
