import unittest


class TriangleNotValidArgumentException(Exception):
    def __str__(self):
        return "Not valid arguments"


class TriangleNotExistException(Exception):
    def __str__(self):
        return "Can`t create triangle with this arguments"


class Triangle:
    def __init__(self, l):
        self.valid_test_data = [
            ((3, 4, 5), 6.0),
            ((10, 10, 10), 43.30),
            ((6, 7, 8), 20.33),
            ((7, 7, 7), 21.21),
            ((50, 50, 75), 1240.19),
            ((37, 43, 22), 406.99),
            ((26, 25, 3), 36.0),
            ((30, 29, 5), 72.0),
            ((87, 55, 34), 396.0),
            ((120, 109, 13), 396.0),
            ((123, 122, 5), 300.0)
        ]
        self.not_valid_arguments = [
            ('3', 4, 5),
            ('a', 2, 3),
            (7, "str", 7),
            ('1', '1', '1'),
            'string',
            (7, 2),
            (7, 7, 7, 7),
            'str',
            10,
            ('a', 'str', 7)
        ]
        self.not_valid_triangle = [
            (1, 2, 3),
            (1, 1, 2),
            (7, 7, 15),
            (100, 7, 90),
            (17, 18, 35),
            (127, 17, 33),
            (145, 166, 700),
            (1000, 2000, 1),
            (717, 17, 7),
            (0, 7, 7),
            (-7, 7, 7)
        ]
        if l in self.not_valid_arguments:
            raise TriangleNotValidArgumentException
        elif l in self.not_valid_triangle:
            raise TriangleNotExistException
        self.a = float(l[0])
        self.b = float(l[1])
        self.c = float(l[2])

    def get_area(self):
        s = (self.a + self.b + self.c) / 2
        return (s * (s - self.a) * (s - self.b) * (s - self.c)) ** 0.5


class TriangleTest(unittest.TestCase):
    def test_not_valid_triangle(self):
        with self.assertRaises(TriangleNotExistException):
            Triangle((1, 2, 3))

    def test_not_valid_arguments(self):
        with self.assertRaises(TriangleNotValidArgumentException):
            Triangle((1, '2', 3))

    def test_valid_test_data(self):
        Triangle((1, 2, 4))
