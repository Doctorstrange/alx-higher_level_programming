#!/usr/bin/python3
"""unitest for base.py"""

import json
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square

class Testto_json_string(unittest.TestCase):
    """unittest for json_string"""
    def test_empty_list(self):
        # Test when the input list is empty
        result = Base.to_json_string([])
        self.assertEqual(result, "[]")

    def test_none_input(self):
        # Test when the input is None
        result = Base.to_json_string(None)
        self.assertEqual(result, "[]")

    def test_valid_input(self):
        # Test with a valid list of dictionaries
        data = [
            {"name": "femi", "age": 31},
            {"name": "ashley", "age": 28},
        ]
        expected_json = json.dumps(data)

        result = Base.to_json_string(data)
        self.assertEqual(result, expected_json)

    def testsquare_two_dicts(self):
        s1 = Square(8, 3, 4, 2)
        s2 = Square(5, 7, 2, 8)
        dic_list = [s1.to_dictionary(), s2.to_dictionary()]
        self.assertTrue(len(Base.to_json_string(dic_list)) == 76)

class TestSaveToFile(unittest.TestCase):

    def test_empty_list(self):
        empty_list = []
        Base.save_to_file(empty_list)

        with open("Base.json", "r") as jsonfile:
            content = jsonfile.read()
            self.assertEqual(content, "[]")

    def testfile_with_data(self):
        class ExampleObject:
            def __init__(self, name):
                self.name = name

            def to_dictionary(self):
                return {"name": self.name}

        data = [ExampleObject("femi"), ExampleObject("ashley")]
        Base.save_to_file(data)

        with open("Base.json", "r") as jsonfile:
            content = jsonfile.read()
            expected_json = json.dumps([{"name": "femi"}, {"name": "ashley"}])
            self.assertEqual(content, expected_json)

class TestFromJsonString(unittest.TestCase):

    def testjson_string_valid_json(self):
        # Test parsing a valid JSON string
        json_string = '[{"name": "femi", "age": 31}, {"name": "ashley", "age": 27}]'
        expected_list = [{"name": "femi", "age": 31}, {"name": "ashley", "age": 27}]
        result = Base.from_json_string(json_string)
        self.assertEqual(result, expected_list)

    def testjson_string_none_input(self):
        # Test parsing None as input
        result = Base.from_json_string(None)
        self.assertEqual(result, [])


class TestLoadFromFile(unittest.TestCase):

    def testcreatefile(self):
        data = [{"name": "femi", "age": 31}, {"name": "ashley", "age": 27}]
        with open("Base.json", "w") as jsonfile:
            jsonfile.write(json.dumps(data))

    def testremovefile(self):
        import os
        os.remove("Base.json")


class TestCreate(unittest.TestCase):

    def test_create_rectangle(self):
        dictionary = {"width": 5, "height": 10}
        instance = Rectangle.create(**dictionary)
        self.assertIsInstance(instance, Rectangle)
        self.assertEqual(instance.width, 5)
        self.assertEqual(instance.height, 10)

    def test_create_square(self):
        dictionary = {"size": 7}
        instance = Square.create(**dictionary)
        self.assertIsInstance(instance, Square)
        self.assertEqual(instance.size, 7)


if __name__ == '__main__':
    unittest.main()
