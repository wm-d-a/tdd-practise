import unittest
import sys, os

sys.path.append(os.getcwd())
from main import *


class TestTDDPractise(unittest.TestCase):
    def test_func_str_given_returns_answer(self):
        self.assertEqual(func('00101110000110'), 4)
        self.assertEqual(func('001011100100000'), 5)
        self.assertEqual(func('100000011100100001'), 6)

    def test_func_not_str_given_returns_error(self):
        self.assertEqual(func(True), -1)
        self.assertEqual(func(17), -1)
        self.assertEqual(func(4.2), -1)


if __name__ == '__main__':
    unittest.main()
