"""
test for Rectangle class
"""
import unittest
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    def test_with_id(self):
        """
        test 1
        :return: nothing
        """
        r3 = Rectangle(10, 2, 0, 0, 12)
        self.assertEqual(r3.id, 12)

    def test_valid_attributes(self):
        """
        test 2
        :return: nothing
        """
        obj = Rectangle(5, 10, 2, 3)
        self.assertEqual(obj.width, 5)
        self.assertEqual(obj.height, 10)
        self.assertEqual(obj.x, 2)
        self.assertEqual(obj.y, 3)

    def test_invalid_attributes(self):
        """
        test 3
        :return: nothing
        """
        with self.assertRaises(TypeError):
            Rectangle("invalid", 10, 2, 3)
        with self.assertRaises(ValueError):
            Rectangle(-5, 10, 2, 3)
        with self.assertRaises(TypeError):
            Rectangle(5, "invalid", 2, 3)
        with self.assertRaises(ValueError):
            Rectangle(5, 0, 2, 3)
        with self.assertRaises(TypeError):
            Rectangle(5, 10, "invalid", 3)
        with self.assertRaises(ValueError):
            Rectangle(5, 10, -2, 3)
        with self.assertRaises(TypeError):
            Rectangle(5, 10, 2, "invalid")
        with self.assertRaises(ValueError):
            Rectangle(5, 10, 2, -3)

    def test_area(self):
        """
        test 4
        :return: nothing
        """
        r1 = Rectangle(3, 2)
        r2 = Rectangle(2, 10)
        r3 = Rectangle(8, 7, 0, 0, 12)
        self.assertEqual(r1.area(), 6)
        self.assertEqual(r2.area(), 20)
        self.assertEqual(r3.area(), 56)

    def test_update_with_args(self):
        """
        test 5
        :return: nothing
        """
        r = Rectangle(2, 3, 1, 1, 1)
        r.update(4, 5, 6, 7, 8)
        self.assertEqual(r.id, 4)
        self.assertEqual(r.width, 5)
        self.assertEqual(r.height, 6)
        self.assertEqual(r.x, 7)
        self.assertEqual(r.y, 8)

    def test_update_with_kwargs(self):
        """
        test 7
        :return: nothing
        """
        r = Rectangle(2, 3, 1, 1, 1)
        r.update(width=5, height=6, x=7, y=8, id=4)
        self.assertEqual(r.id, 4)
        self.assertEqual(r.width, 5)
        self.assertEqual(r.height, 6)
        self.assertEqual(r.x, 7)
        self.assertEqual(r.y, 8)


if __name__ == '__main__':
    unittest.main()
