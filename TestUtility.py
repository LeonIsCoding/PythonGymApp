import unittest
from Utility import Utility


class MyTestCase(unittest.TestCase):
    def test_roundvalue(self):
        self.assertEqual(10, Utility.roundvalue(0, 9.51))
        self.assertEqual(9, Utility.roundvalue(0, 9.49))
        self.assertEqual(10.5, Utility.roundvalue(1, 10.457))
        self.assertEqual(10.4, Utility.roundvalue(1, 10.44))
        self.assertEqual(15.35, Utility.roundvalue(2, 15.354))
        self.assertEqual(15.34, Utility.roundvalue(2, 15.336))
