#!/usr/bin/python3
"""Unittests for max_integer([..])"""
import unittest
max_integer = __import__('6-max_integer').max_integer
class TestMaxInteger(unittest.TestCase):
	"""unittests for max_integer([..])."""
	def test_ordered_list(self):
		"""ordered list of integers."""
		ordered = [1, 2, 3, 4, 5]
		self.assertEqual(max_integer(ordered), 5)

	def test_max_at_begginning(self):
		"""list with a beginning max value."""
		max_at_beginning = [6, 5, 4, 3, 2, 1]
		self.assertEqual(max_integer(max_at_beginning), 6)

	def test_unordered_list(self):
		"""unordered list of integers"""
		unordered = [1, 2, 4, 3, 5, 9, 8]
		self.assertEqual(max_integer(unordered), 9)

	def test_one_element_list(self):
		"""list with a single element."""
		one_element = [5]
		self.assertEqual(max_integer(one_element), 5)

	def test_empty_string(self):
		"""empty string."""
		self.assertEqual(max_integer(""), None)
if __name__ == '__main__':
    unittest.main()
