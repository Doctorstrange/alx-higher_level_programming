#!/usr/bin/python3
"""Defines an object attribute lookup function."""


def lookup(obj):
    """Returns list of available objects"""
    return (dir(obj))
