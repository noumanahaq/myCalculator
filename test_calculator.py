import unittest
from main import MyCalculator

class TestMyCalculator(unittest.TestCase):

    def setUp(self):
        """Initialize the calculator before each test."""
        self.calculator = MyCalculator()

    def test_add(self):
        self.assertEqual(self.calculator.add(2, 3), 5)
        self.assertEqual(self.calculator.add(-1, 1), 0)
        self.assertEqual(self.calculator.add(0, 0), 0)

    def test_subtract(self):
        self.assertEqual(self.calculator.subtract(5, 3), 2)
        self.assertEqual(self.calculator.subtract(0, 5), -5)

    def test_multiply(self):
        self.assertEqual(self.calculator.multiply(2, 3), 6)
        self.assertEqual(self.calculator.multiply(0, 10), 0)

    def test_divide(self):
        self.assertEqual(self.calculator.divide(10, 2), 5)
        self.assertEqual(self.calculator.divide(5, 1), 5)
        self.assertEqual(self.calculator.divide(0, 5), 0)

    def test_divide_by_zero(self):
        self.assertEqual(self.calculator.divide(10, 0), "Error! Division by zero.")

if __name__ == '__main__':
    unittest.main()
