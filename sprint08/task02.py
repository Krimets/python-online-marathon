import unittest
from func_test import divide
class DivideTest(unittest.TestCase):
    def test_possitive_divide(self):
        expected = 5
        actual = divide(10, 2)
        self.assertEqual(actual, expected)

    def test_possitive_divide2(self):
        expected = 0.5
        actual = divide(2, 4)
        self.assertEqual(actual, expected)
    def test_double_possitive_divide(self):
        expected = 0.333333
        actual = divide(1, 3)
        self.assertAlmostEqual(actual, expected, 6)

    def test_raises(self):
        self.assertRaises(Exception, divide, 3, 0)