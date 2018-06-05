import unittest

from AddSubtract.Add import func_add

class AddTest(unittest.TestCase):

    def test_add(self):
        self.assertEqual(func_add(10,12), 22)
