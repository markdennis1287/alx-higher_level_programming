"""
Test for Base class
"""
import unittest
import json
from models.base import Base
from models.rectangle import Rectangle
import os


class TestBase(unittest.TestCase):
    """
    Class TestBase
    """
    def test_with_id(self):
        """
        test 1
        :return: nothing
        """
        b1 = Base(12)
        self.assertEqual(b1.id, 12)

    def test_without_id(self):
        """
        test 2
        :return: nothing
        """
        b2 = Base()
        b3 = Base()
        self.assertEqual(b2.id, 1)
        self.assertEqual(b3.id, 2)

    def setUp(self):
        """
        test 3
        :return: nothing
        """
        Base._Base__nb_objects = 0

    def test_save_to_file(self):
        """
        test 4
        :return: nothing
        """
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        list_rectangles_input = [r1, r2]

        Rectangle.save_to_file(list_rectangles_input)

        with open("Rectangle.json", "r") as file:
            data = json.load(file)
            self.assertEqual(data, [r1.to_dictionary(), r2.to_dictionary()])

    def test_load_from_file(self):
        """
        test 5
        :return: nothing
        """
        if os.path.isfile("Rectangle.json"):
            os.remove("Rectangle.json")
        if os.path.isfile("Square.json"):
            os.remove("Square.json")

        list_rectangles_output = Rectangle.load_from_file()
        self.assertEqual(list_rectangles_output, [])

        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        list_rectangles_input = [r1, r2]

        Rectangle.save_to_file(list_rectangles_input)

        list_rectangles_output = Rectangle.load_from_file()
        self.assertEqual(len(list_rectangles_output), 2)
        self.assertIsInstance(list_rectangles_output[0], Rectangle)
        self.assertIsInstance(list_rectangles_output[1], Rectangle)
        self.assertEqual(list_rectangles_output[0].width, r1.width)
        self.assertEqual(list_rectangles_output[0].height, r1.height)
        self.assertEqual(list_rectangles_output[0].x, r1.x)
        self.assertEqual(list_rectangles_output[0].y, r1.y)
        self.assertEqual(list_rectangles_output[1].width, r2.width)
        self.assertEqual(list_rectangles_output[1].height, r2.height)
        self.assertEqual(list_rectangles_output[1].x, r2.x)
        self.assertEqual(list_rectangles_output[1].y, r2.y)

    def test_save_to_file_csv(self):
        """
        test 6
        :return: nothing
        """
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        list_rectangles_input = [r1, r2]

        Rectangle.save_to_file_csv(list_rectangles_input)

    def test_load_from_file_csv(self):
        """
        test 7
        :return: nothing
        """
        if os.path.isfile("Rectangle.csv"):
            os.remove("Rectangle.csv")
        if os.path.isfile("Square.csv"):
            os.remove("Square.csv")

        list_rectangles_output = Rectangle.load_from_file_csv()
        self.assertEqual(list_rectangles_output, [])

        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        list_rectangles_input = [r1, r2]

        Rectangle.save_to_file_csv(list_rectangles_input)

        list_rectangles_output = Rectangle.load_from_file_csv()
        self.assertEqual(len(list_rectangles_output), 2)
        self.assertIsInstance(list_rectangles_output[0], Rectangle)
        self.assertIsInstance(list_rectangles_output[1], Rectangle)
        self.assertEqual(list_rectangles_output[0].width, r1.width)
        self.assertEqual(list_rectangles_output[0].height, r1.height)
        self.assertEqual(list_rectangles_output[0].x, r1.x)
        self.assertEqual(list_rectangles_output[0].y, r1.y)
        self.assertEqual(list_rectangles_output[1].width, r2.width)
        self.assertEqual(list_rectangles_output[1].height, r2.height)
        self.assertEqual(list_rectangles_output[1].x, r2.x)
        self.assertEqual(list_rectangles_output[1].y, r2.y)


if __name__ == '__main__':
    unittest.main()
