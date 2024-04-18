#!/usr/bin/python3
"""
Module containing Mylist class
"""


class MyList (list):
    def print_sorted(self):
        sort_list = sorted(self)
        print(sort_list)
