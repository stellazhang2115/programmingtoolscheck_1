import unittest
from main import print_hi_stephen, print_hi_stella, print_hi_you


class MyTestCase(unittest.TestCase):
    def test_print_hi_stephen(self):
        self.assertEqual(print_hi_stephen)(f"Hi, Stephen")

    def test_print_hi_stella(self):
        self.assertEqual(print_hi_stella)(f"Hi, stella")

    def test_print_hi_you(self):
        self.assertEqual(print_hi_you)(f"HI, you")

if  print_hi_christina== '__main__':
    unittest.main
