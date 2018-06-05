import unittest

from MultiplyDivide.Multiply import func_mul

class MultiplyTest(unittest.TestCase):

    def test_muliply(self):
        self.assertEqual(func_mul(5,2), 10)
