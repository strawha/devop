from calculator import sum,divide,multiply,diff
import unittest

class CalculatorTest(unittest.TestCase):
    def test_sum(self):
        assert sum(1,3) == 4

    def test_diff(self):
        assert diff(4,2) == 2

    def test_multiply(self):
        assert multiply(2,3) == 6
        assert multiply(0,2) == 0

    def test_divide(self):
        assert divide(4,2) == 2
