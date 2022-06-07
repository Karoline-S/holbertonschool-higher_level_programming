#!/usr/bin/python3
"""
Contains tests for Rectangle class - Task 2
Focus is on:
- setting private instance attributes in the constructor using
  getters and setters
- calling super()__init__() to set public instance id attribute
"""

import unittest
import inspect
import pycodestyle

from models.base import Base
from models import rectangle
Rectangle = rectangle.Rectangle


class TestRectangleDocs(unittest.TestCase):
    """Tests for documentation of class"""

    @classmethod
    def setUpClass(cls):
        """Set up for the doc tests"""
        cls.rect_funcs = inspect.getmembers(Rectangle, inspect.isfunction)

    def test_conformance_class(self):
        """Test that we conform to Pycodestyle."""
        style = pycodestyle.StyleGuide(quiet=True)
        result = style.check_files(['models/rectangle.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_conformance_test(self):
        """Test that we conform to Pycodestyle."""
        style = pycodestyle.StyleGuide(quiet=True)
        result = style.check_files(['tests/test_models/test_rectangle.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_module_docstr(self):
        """Tests for docstring"""
        self.assertTrue(len(rectangle.__doc__) >= 1)

    def test_class_docstr(self):
        """Tests for docstring"""
        self.assertTrue(len(Rectangle.__doc__) >= 1)

    def test_func_docstr(self):
        """Tests for docstrings in all functions"""
        for func in self.rect_funcs:
            self.assertTrue(len(func[1].__doc__) >= 1)


class TestRectangle(unittest.TestCase):
    """ Tests initialisation, getters and setters"""

    def test_properties(self):
        """Tests all setters and getters"""
        Base._Base__nb_objects = 0
        r_1 = Rectangle(1, 1)
        self.assertEqual(r_1.width, 1)
        self.assertEqual(r_1.height, 1)
        self.assertEqual(r_1.x, 0)
        self.assertEqual(r_1.y, 0)

        r_1.x = 10
        r_1.y = 10
        self.assertEqual(r_1.x, 10)
        self.assertEqual(r_1.y, 10)

    def test_width_type(self):
        """tests width as non-int"""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle("4", 4, 4, 4)

    def test_width_value_zero(self):
        """test width as 0"""
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Rectangle(0, 4)

    def test_width_value_neg(self):
        """test width as negative"""
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Rectangle(-4, 4)

    def test_height_type(self):
        """test height as non-int"""
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(4, [4])

    def test_height_zero(self):
        """test height as zero"""
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            Rectangle(4, 0)

    def Test_height_value_neg(self):
        """test height as negative"""
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            Rectangle(4, -4)

    def test_x_type(self):
        """test x as non-int"""
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(4, 4, 'x')

    def test_x_value(self):
        """test x as negative"""
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            Rectangle(4, 4, -4)

    def test_y_type(self):
        """test y as non-int"""
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(4, 4, 4, (4, 4))

    def test_y_value(self):
        """test y as negative"""
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            Rectangle(4, 4, 4, -4)

    """ Tests functionality of super()__init__() call"""

    def test_id_none(self):
        """Tests id not passed in"""
        Base._Base__nb_objects = 0
        r_2 = Rectangle(1, 1)
        self.assertEqual(r_2.id, 1)

    def test_id_assigned(self):
        """Tests id passed in"""
        r_3 = Rectangle(1, 1, 1, 1, 88)
        self.assertEqual(r_3.id, 88)

    def test_nb_object_increment(self):
        """Tests private class attribute incrementation"""
        Base._Base__nb_objects = 0
        r_4 = Rectangle(1, 1)
        r_5 = Rectangle(1, 1)
        r_6 = Rectangle(1, 1, 1, 1, 55)
        r_7 = Rectangle(1, 1)
        self.assertEqual(r_7.id, 3)

    """Tests number of arguments passed in"""
    def test_too_many_args(self):
        """Tests entering too many args to instantiate object"""
        with self.assertRaises(TypeError):
            r = Rectangle(1, 2, 3, 4, 5, 6)

    def test_too_few_args(self):
        """Tests entering too few args to instantiate object"""
        with self.assertRaises(TypeError):
            r = Rectangle()

    def tes_area_method(self):
        """tests the method area"""
        r_1 = Rectangle(5, 5)
        self.assertEqual(r_1.area(), 25)

    def test_update_method_args(self):
        """tests the update method"""
        r_1 = Rectangle(5, 5, 5, 5, 88)
        r_1.update(55, 8, 9, 10, 11)
        self.assertEqual(r_1.id, 55)
        self.assertEqual(r_1.width, 8)
        self.assertEqual(r_1.height, 9)
        self.assertEqual(r_1.x, 10)
        self.assertEqual(r_1.y, 11)

    def test_update_method_kwargs(self):
        """tests the udpate method with kwargs"""
        r_1 = Rectangle(5, 5, 5, 5, 88)
        r_1.update(x=10, height=10)
        self.assertEqual(r_1.id, 88)
        self.assertEqual(r_1.width, 5)
        self.assertEqual(r_1.height, 10)
        self.assertEqual(r_1.x, 10)
        self.assertEqual(r_1.y, 5)

    def test_udpate_method_both(self):
        """tests the update method with args and kwargs"""
        r_1 = Rectangle(5, 5, 5, 5, 88)
        r_1.update(44, width=10)
        self.assertEqual(r_1.id, 44)
        self.assertEqual(r_1.width, 5)
        self.assertEqual(r_1.height, 5)
        self.assertEqual(r_1.x, 5)
        self.assertEqual(r_1.y, 5)

#    def test_display_method(self):
#        """tests the method display"""
