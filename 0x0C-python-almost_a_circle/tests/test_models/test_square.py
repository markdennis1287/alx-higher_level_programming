"""
tests for Square class
"""
import unittest
from models.square import Square


class TestSquare(unittest.TestCase):
    def test_with_id(self):
        """
        test 1
        :return: nothing
        """
        r3 = Square(10, 0, 0, 12)
        self.assertEqual(r3.id, 12)

    def test_valid_attributes(self):
        """
        test 2
        :return: nothing
        """
        obj = Square(5, 2, 3)
        self.assertEqual(obj.width, 5)
        self.assertEqual(obj.height, 5)
        self.assertEqual(obj.x, 2)
        self.assertEqual(obj.y, 3)

    def test_invalid_attributes(self):
        """
        test 3
        :return: nothing
        """
        with self.assertRaises(TypeError):
            Square("invalid", 2, 3)
        with self.assertRaises(ValueError):
            Square(-5, 2, 3)
        with self.assertRaises(TypeError):
            Square(5, "invalid", 3)
        with self.assertRaises(ValueError):
            Square(5, -2, 3)
        with self.assertRaises(TypeError):
            Square(5, 2, "invalid")
        with self.assertRaises(ValueError):
            Square(5, 2, -3)

    def test_area(self):
        """
        test 4
        :return: nothing
        """
        r1 = Square(3)
        r2 = Square(2)
        r3 = Square(8, 0, 0, 12)
        self.assertEqual(r1.area(), 9)
        self.assertEqual(r2.area(), 4)
        self.assertEqual(r3.area(), 64)

    def test_update_with_args(self):
        """
        test 5
        :return: nothing
        """
        r = Square(2, 1, 1, 1)
        r.update(4, 6, 7, 8)
        self.assertEqual(r.id, 4)
        self.assertEqual(r.width, 6)
        self.assertEqual(r.height, 6)
        self.assertEqual(r.x, 7)
        self.assertEqual(r.y, 8)

    def test_update_with_kwargs(self):
        """
        test 6
        :return: nothing
        """
        r = Square(2, 1, 1, 1)
        r.update(size=5, x=7, y=8, id=4)
        self.assertEqual(r.id, 4)
        self.assertEqual(r.width, 5)
        self.assertEqual(r.height, 5)
        self.assertEqual(r.x, 7)
        self.assertEqual(r.y, 8)


if __name__ == '__main__':
    unittest.main()
