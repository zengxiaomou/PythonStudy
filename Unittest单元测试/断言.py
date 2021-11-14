import unittest
from calculator import Calculator

class TestMath(unittest.TestCase):
    def setUp(self):
        print("test start")
    def test_add(self):
        j=Calculator(5,10)
        self.assertEqual(j.add(),15)

    def test_add1(self):
        j = Calculator(5, 10)
        self.assertNotEqual(j.add(),20)

    def tearDown(self):
        print("test down")


if __name__ == '__main__':
    TheApp = 0