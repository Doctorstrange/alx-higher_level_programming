#!/usr/bin/python3
"""Defines a text-indentation function."""


def text_indentation(text):
    """function that prints a text with 2 new lines
    after each of these characters: ., ? and :.
    text must be a string, otherwise raise a
    TypeError exception with the message text must be a string
    There should be no space at the beginning or at the
    end of each printed line
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    x = 0
    while x < len(text) and text[x] == ' ':
        x += 1

    while x < len(text):
        print(text[x], end="")
        if text[x] == "\n" or text[x] in ".?:":
            if text[x] in ".?:":
                print("\n")
            x += 1
            while x < len(text) and text[x] == ' ':
                x += 1
            continue
        x += 1
