#!/usr/bin/python3
""" the first class Base"""
import json


class Base:
    """the “base” of all other classes in this project"""

    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """that returns the JSON string representation of list_dictionaries:
        Return: the JSON string representation of list_dictionaries
        """
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """class Base by adding the class method def save_to_file(cls,
        list_objs): that writes the JSON string representation
        of list_objs to a file:
        """
        filename = cls.__name__ + ".json"
        with open(filename, "w") as jsonfile:
            if list_objs is None:
                jsonfile.write("[]")
            else:
                dic_list = []
                for o in list_objs:
                    dic_list.append(o.to_dictionary())
                jsonfile.write(Base.to_json_string(dic_list))

    @staticmethod
    def from_json_string(json_string):
        """Update the class Base by adding the static method def
        from_json_string(json_string): that returns the list of
        the JSON string representation json_string:
        Return: the list represented by json_string
        """
        if json_string is None or json_string == "[]":
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """returns an instance with all attributes already set:
        """
        if dictionary and dictionary != {}:
            if cls.__name__ == "Rectangle":
                new = cls(1, 1)
            else:
                new = cls(1)
            new.update(**dictionary)
            return new

    @classmethod
    def load_from_file(cls):
        """Update the class Base by adding the class
        method def load_from_file(cls): that returns a list of instances:
        """
        filename = str(cls.__name__) + ".json"
        try:
            with open(filename, "r") as jsonfile:
                dic_list = Base.from_json_string(jsonfile.read())
                return [cls.create(**d) for d in dic_list]
        except IOError:
            return []
