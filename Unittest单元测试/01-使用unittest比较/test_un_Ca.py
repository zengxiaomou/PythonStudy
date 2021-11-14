import unittest
from calculator import Calculator

class TestCalculator(unittest.TestCase):
    def test_add(self):
        c = Calculator(3, 5)
        result = c.add()
        self.assertEqual(result, 8)
    def test_sub(self):
        c = Calculator(7, 5)
        result = c.sub()
        self.assertEqual(result, 2)

if __name__ == '__main__':
    unittest.main()
