import unittest

from AddSubtract.Subtract import func_substract

class SubtractTest(unittest.TestCase):

    def test_subract(self):
        self.assertEqual(func_substract(20,11), 9)
