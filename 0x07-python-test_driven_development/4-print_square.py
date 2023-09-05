#!/usr/bin/python3
"""Defines a square-printing function."""


def print_square(size):
    """prints a square with the character #
    size is the size length of the square
    size must be an integer, otherwise raise a
    TypeError exception with the message size must be an integer
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if isinstance(size, float) or size < 0:
        raise TypeError("size must be an integer")

    for x in range(size):
        [print("#", end="") for y in range(size)]
        print("")
