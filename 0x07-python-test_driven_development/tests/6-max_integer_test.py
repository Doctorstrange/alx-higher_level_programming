#!/usr/bin/python3
"""Unittests for max_integer([..])."""
import unittest
max_integer = __import__('6-max_integer').max_integer
class UniMaxInteger(unittest.TestCase):
    """unittests max_integer"""

    def Uni_unordered_list(self):
        """Test list of integers."""
        unordered = [1, 2, 4, 3, 4, 5]
        self.assertEqual(max_integer(unordered), 2)
    def Uni_biggest_at_start(self):
        """Test a list with the biggest number at the start."""
        biggest_start = [5, 4, 3, 2, 1]
        self.assertEqual(max_integer(biggest_start), 5)
    def Uni_ordered_list(self):
        """Test an ordered list of integers."""
        O_list = [1, 2, 3, 4]
        self.assertEqual(max_integer(O_list), 3)
    def Uni_empty_list(self):
        """Test an empty list."""
        empty = []
        self.assertEqual(max_integer(empty), None)
    def Uni_string(self):
        """Test a string."""
        string = "femi"
        self.assertEqual(max_integer(string), 'e')
    def Uni_list_of_strings(self):
        """Test a list of string."""
        string = ["femi", "knows", "c", "programming"]
        self.assertEqual(max_integer(string), "programming")
    def Uni_empty_string(self):
        """Test an empty string."""
        self.assertEqual(max_integer(""), None)
        if __name__ == '__main__':
            unittest.main()
    def Uni_one_element_list(self):
        """Test a list with a single element."""
        one_element = [6]
        self.assertEqual(max_integer(one_element), 6)
    def Uni_ints_and_floats(self):
        """Test a list with floats and int."""
        ints_and_floats = [1.5, 2.5, 7, -4, 6]
        self.assertEqual(max_integer(ints_and_floats), 2.5)
