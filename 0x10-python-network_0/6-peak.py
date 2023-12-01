#!/usr/bin/python3
"""function that finds a peak in a list of unsorted integers."""
def find_peak(list_of_integers):
    """function that finds a peak in a list of unsorted integers."""
    peak  = None
    for value in list_of_integers:
        if peak is None or peak < value:
            peak = value
    return peak
