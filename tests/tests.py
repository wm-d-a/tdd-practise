import unittest
import sys, os

sys.path.append(os.getcwd())
from main import *


class TestTDDPractise(unittest.TestCase):
    def test_func_str_given_returns_answer(self):
        self.assertEqual(func('00101110000110'), 4)
        self.assertEqual(func('001011100100000'), 5)


if __name__ == '__main__':
    unittest.main()
