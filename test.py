import unittest


class Test(unittest.TestCase):
    # Returns the correct sum of two positive integers
    def test_sum_of_two_positive_integers(self):
        result = sum(3, 5)
        self.assertEqual(result, 8)

    def test_sum_of_large_integers(self):
        large_number = 10 ** 18
        result = sum(large_number, large_number)
        self.assertEqual(result, 2 * large_number)