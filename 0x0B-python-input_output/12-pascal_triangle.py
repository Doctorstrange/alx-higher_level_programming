#!/usr/bin/python3
"""representing the Pascal’s triangle of n"""


def pascal_triangle(n):
    """representing the Pascal’s triangle of n.

    Returns a list of lists of integers representing the Pascal’s triangle of n.
    """
    if n <= 0:
        return []

    angle = [[1]]
    while len(angle) != n:
        tri = angle[-1]
        tmp = [1]
        for i in range(len(tri) - 1):
            tmp.append(tri[i] + tri[i + 1])
        tmp.append(1)
        angle.append(tmp)
    return (angle)
