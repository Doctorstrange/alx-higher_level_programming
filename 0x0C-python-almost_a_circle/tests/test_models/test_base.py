#!/usr/bin/python3
"""unitest for base.py"""

import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square

class Testto_json_string(unittest.TestCase):
    """unittest for json_string"""
    def test_empty_list(self):
        # Test when the input list is empty
        result = YourClass.to_json_string([])
        self.assertEqual(result, "[]")

    def test_none_input(self):
        # Test when the input is None
        result = YourClass.to_json_string(None)
        self.assertEqual(result, "[]")

    def test_valid_input(self):
        # Test with a valid list of dictionaries
        data = [
            {"name": "Alice", "age": 30},
            {"name": "Bob", "age": 25},
        ]
        expected_json = json.dumps(data)  # Expected JSON representation

        result = YourClass.to_json_string(data)
        self.assertEqual(result, expected_json)

if __name__ == '__main__':
    unittest.main()
