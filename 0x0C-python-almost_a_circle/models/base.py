#!/usr/bin/python3
"""
Module containing Base class
"""
import json
import csv
import turtle


class Base:
    """
    Base class
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """
        Initialize base
        :param id: id
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        Json encode to string.
        :param list_dictionaries: dictionaries to encode
        :return: Encoded dictionary.
        """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        Save to file JSON.
        :param list_objs: obj list
        :return: nothing.
        """
        filename = cls.__name__ + ".json"
        if list_objs is None:
            list_objs = []
        json_list = [obj.to_dictionary() for obj in list_objs]
        json_string = cls.to_json_string(json_list)
        with open(filename, "w") as file:
            file.write(json_string)

    @staticmethod
    def from_json_string(json_string):
        """
        JSON decode JSON-string.
        :param json_string: string
        :return: Decoded string.
        """
        if json_string is None or json_string == "":
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """
        Dummy dict.
        :param dictionary: dict
        :return: dummy_instance.
        """
        if cls.__name__ == "Rectangle":
            dummy_instance = cls(1, 1)  # Create a dummy Rectangle instance
        elif cls.__name__ == "Square":
            dummy_instance = cls(1)  # Create a dummy Square instance
        else:
            dummy_instance = None

        if dummy_instance is not None:
            dummy_instance.update(**dictionary)  # Call update with dictionary
        return dummy_instance

    @classmethod
    def load_from_file(cls):
        """
        JSON load from file.
        :return: Empty list if no file else instances.
        """
        filename = cls.__name__ + ".json"
        try:
            with open(filename, "r") as file:
                json_string = file.read()
                dictionaries = cls.from_json_string(json_string)
                instances = [cls.create(**dictionary) for dictionary in
                             dictionaries]
                return instances
        except FileNotFoundError:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """
        Csv saving.
        :param list_objs: obj list
        :return: nothing.
        """
        filename = cls.__name__ + ".csv"
        with open(filename, 'w', newline='') as file:
            writer = csv.writer(file)
            if list_objs is None or len(list_objs) == 0:
                writer.writerow([])
            else:
                if cls.__name__ == "Rectangle":
                    fieldnames = ["id", "width", "height", "x", "y"]
                elif cls.__name__ == "Square":
                    fieldnames = ["id", "size", "x", "y"]
                writer.writerow(fieldnames)
                for obj in list_objs:
                    writer.writerow([getattr(obj, field) for
                                     field in fieldnames])

    @classmethod
    def load_from_file_csv(cls):
        """
        Csv loading.
        :return: instances.
        """
        filename = cls.__name__ + ".csv"
        instances = []
        try:
            with open(filename, 'r', newline='') as file:
                reader = csv.reader(file)
                fields = next(reader)
                for row in reader:
                    args = [int(value) for value in row]
                    instance = cls.create(**dict(zip(fields, args)))
                    instances.append(instance)
        except FileNotFoundError:
            return instances
        return instances

    @staticmethod
    def draw(list_rectangles, list_squares):
        """
        Tutle stuff.
        :param list_rectangles: rectangles
        :param list_squares: squares
        :return: nothing.
        """
        screen = turtle.Screen()
        screen.setup(800, 600)
        pen = turtle.Turtle()

        for rectangle in list_rectangles:
            pen.penup()
            pen.goto(rectangle.x, rectangle.y)
            pen.pendown()
            pen.color("blue")
            pen.forward(rectangle.width)
            pen.left(90)
            pen.forward(rectangle.height)
            pen.left(90)
            pen.forward(rectangle.width)
            pen.left(90)
            pen.forward(rectangle.height)
            pen.left(90)

        for square in list_squares:
            pen.penup()
            pen.goto(square.x, square.y)
            pen.pendown()
            pen.color("red")
            pen.forward(square.size)
            pen.left(90)
            pen.forward(square.size)
            pen.left(90)
            pen.forward(square.size)
            pen.left(90)
            pen.forward(square.size)
            pen.left(90)

        turtle.done()
