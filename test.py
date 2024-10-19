import unittest

from main import custom_sum


class Test(unittest.TestCase):
    # Returns the correct sum for two positive integers
    def test_sum_of_two_positive_integers(self):
        result = custom_sum(3, 5)
        self.assertEqual(result, 8)

    # Handles very large integers without overflow
    def test_large_integer_sum(self):
        large_num1 = 10 ** 18
        large_num2 = 10 ** 18
        result = custom_sum(large_num1, large_num2)
        self.assertEqual(result, 2 * 10 ** 18)

