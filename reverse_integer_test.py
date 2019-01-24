import unittest
from reverse_iteger import Solution

class reverse_integer_test(unittest.TestCase):
    def reverse_integer_function_test(self):
        test_integer = -123
        expected_result = -321
        solution = Solution()
        result = solution.reverseInteger(test_integer)
        self.assertEqual(expected_result, result)
