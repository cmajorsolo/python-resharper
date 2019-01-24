import unittest
from zigzag_conversion import Solution

class zigzag_converstion_test(unittest.TestCase):
    def conversion_test(self):
        test_string = 'PAYPALISHIRING'
        test_row_number = 4
        solution = Solution()
        actual_result = solution.convert(test_string, test_row_number)
        expected_result = 'PINALSIGYAHRPI'
        self.assertEqual(actual_result, expected_result)