import unittest

from MultiplyDivide.Divide import func_div

class DivideTest(unittest.TestCase):

    def test_divide(self):
        self.assertEqual(func_div(5,2), 2)
        self.assertEqual(func_div(7,2), 3)
