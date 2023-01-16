import unittest
import math


def quadratic_equation(a, b, c):
    if a == 0 and b == 0 and c == 0:
        raise ValueError
    dis = b * b - 4 * a * c
    sqrt_val = math.sqrt(abs(dis))
    if dis > 0:
        return ((-b + sqrt_val) / (2 * a)), ((-b - sqrt_val) / (2 * a))

    elif dis == 0:
        return -b / (2 * a)

    elif dis < 0:
        return None


class QuadraticEquationTest(unittest.TestCase):

    def test_quadratic_equation(self):
        expected = 0
        actual = quadratic_equation(1, -4, 4)
        self.assertTrue(expected < actual)

    def test_quadratic_equation2(self):
        expected = 0
        actual = quadratic_equation(1, -4, 4)
        self.assertTrue(expected < actual)

    def test_quadratic(self):
        expected = 0
        actual = quadratic_equation(1, -4, 4)
        self.assertTrue(expected < actual)

    def test_raises(self):
        self.assertRaises(Exception, quadratic_equation, 0, 0)

try:
    quadratic_equation(0, 0, 0)
except ValueError:
    print('error')