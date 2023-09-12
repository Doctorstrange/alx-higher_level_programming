#!/usr/bin/python3
""" class MyList that inherits from list"""


class MyList(list):
    """calls printing of the list."""

    def print_sorted(self):
        """Print a list in ascending order"""
        print(sorted(self))
