#!/usr/bin/python3
"""
Unittest for "base.py"
Execute all tests: python3 -m unittest discover tests
Execute this test: python3 -m unittest tests/test_models/test_base.py
"""

import unittest
import pycodestyle
from models import base
Base = base.Base


class TestBase(unittest.TestCase):
    """
    class that test the max integer function
    Task 1:
        you can assume id is an integer and you don’t need to test the
            type of it
    Tests:
        test_many_created (working test):
            no arguments when created Base
            None arguments when created Base
            Random integer argument when created Base
            negative integer when creating Base
            double same id when creating Base
        test_too_many_arguments (no-working test):
            too many arguments given
    """
    def setUp(self):
        """Set the instance at 0"""
        Base._Base__nb_objects = 0
        pass

    def tearDown(self):
        """Set the instance at 0"""
        pass

    def test_documentation(self):
        """test all documentation of module"""
        # module documentation
        module = len(base.__doc__)
        self.assertGreater(module, 0)

        # class documentation
        module_class = len(Base.__doc__)
        self.assertGreater(module_class, 0)

        module_class = len(Base.__init__.__doc__)
        self.assertGreater(module_class, 0)

        module_class = len(Base.to_json_string.__doc__)
        self.assertGreater(module_class, 0)

        module_class = len(Base.save_to_file.__doc__)
        self.assertGreater(module_class, 0)

        module_class = len(Base.from_json_string.__doc__)
        self.assertGreater(module_class, 0)

        module_class = len(Base.create.__doc__)
        self.assertGreater(module_class, 0)

        module_class = len(Base.load_from_file.__doc__)
        self.assertGreater(module_class, 0)

    def test_conformance(self):
        """Test that we conform to PEP-8."""
        style = pycodestyle.StyleGuide(quiet=True)
        result = style.check_files(["models/base.py"])
        self.assertEqual(
            result.total_errors, 0, "Found code style errors (pycodestyle)."
        )

    def test_many_created(self):
        """fuction that test for good assignment of differents id value"""
        b1 = Base()
        b2 = Base(None)
        b3 = Base(12)
        b4 = Base()
        b5 = Base(-3)
        b6 = Base(2)
        b7 = Base("Holberthon")
        b8 = Base(4.5)

        self.assertEqual(b1.id, 1)
        self.assertEqual(b2.id, 2)
        self.assertEqual(b3.id, 12)
        self.assertEqual(b4.id, 3)
        self.assertEqual(b5.id, -3)
        self.assertEqual(b6.id, 2)
        self.assertEqual(b7.id, "Holberthon")
        self.assertEqual(b8.id, 4.5)

    def test_too_many_arguments(self):
        """
        fuction that test for TypeError
        """
        with self.assertRaises(TypeError):
            Base(1, 2)

    def test_toJsonString(self):
        """Convert list to Json content"""
        list_json = [{"Salut": 1, "Bonjour": 2}]
        string = Base.to_json_string(list_json)
        self.assertTrue(type(string), str)
        self.assertEqual(string, '[{"Salut": 1, "Bonjour": 2}]')

    def test_toJsonString_empty(self):
        """Convert empty list to Json content"""
        list_json = []
        string = Base.to_json_string(list_json)
        self.assertTrue(type(string), str)
        self.assertEqual(string, '[]')

    def test_toJsonString_None(self):
        """Convert None to Json content"""
        list_json = None
        string = Base.to_json_string(list_json)
        self.assertTrue(type(string), str)
        self.assertEqual(string, '[]')

    def test_fromJsonString(self):
        """Convert Json content to list"""
        string = '[{"Salut": 1, "Bonjour": 2}]'
        list_json = Base.from_json_string(string)
        self.assertTrue(type(list_json), list)
        self.assertEqual(list_json, [{"Salut": 1, "Bonjour": 2}])

    def test_fromJsonStringList(self):
        """Convert Json content to list"""
        string = '[{"Salut": 1, "Bonjour": 2}, {"Hola": 1}]'
        list_json = Base.from_json_string(string)
        self.assertTrue(type(list_json), list)
        self.assertEqual(list_json[0], {"Salut": 1, "Bonjour": 2})
        self.assertEqual(list_json[1], {"Hola": 1})

    def test_fromJsonString_None(self):
        """Convert None Json content to list"""
        string = None
        list_json = Base.from_json_string(string)
        self.assertTrue(type(list_json), list)
        self.assertEqual(list_json, [])

    def test_fromJsonString_len0(self):
        """Convert empty Json content to list"""
        string = ""
        list_json = Base.from_json_string(string)
        self.assertTrue(type(list_json), list)
        self.assertEqual(list_json, [])


if __name__ == "__main__":
    unittest.main()
