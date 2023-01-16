import unittest


class Worker:
    def __init__(self, name, salary=0):
        self.tax = 0.0
        if salary < 0:
            raise ValueError
        self.name = name
        self.salary = salary

    def get_tax_value(self):
        if self.salary <= 1000:
            return float(0.0)
        elif self.salary <= 3000:
            return 0.1 * (self.salary - 1000)
        elif self.salary <= 5000:
            return 0.15 * (self.salary - 3000) + 200
        elif self.salary <= 10000:
            return 0.21 * (self.salary - 5000) + 500
        elif self.salary <= 20000:
            return 0.30 * (self.salary - 10000) + 1550
        elif self.salary <= 50000:
            return 0.40 * (self.salary - 20000) + 4550
        else:
            return 0.47 * (self.salary - 50000) + 16550


class WorkerTest(unittest.TestCase):
    def setUp(self):
        self.my_data = Worker("Natasha", 1001)

    def test_empty(self):
        with self.subTest():
            self.assertEqual(self.my_data.name, "Natasha")

    @unittest.expectedFailure
    def test_raises(self):
        with self.subTest():
            self.assertEqual(self.my_data.salary, -100)

    def tearDown(self):
        self.my_data = None
