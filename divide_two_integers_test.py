import unittest
from divide_two_integers import Solution

class divideTwoIntegersTest(unittest.TestCase):
    # def sample_test_1(self):
    #     solution = Solution()
    #     dividend = 13
    #     divisor = 3
    #     expected_result = 4
    #     actual_results = solution.divide(dividend, divisor)
    #     self.assertEqual(expected_result, actual_results)
    #
    # def sample_test_2(self):
    #     solution = Solution()
    #     dividend = 7
    #     divisor = -3
    #     expected_result = -2
    #     actual_results = solution.divide(dividend, divisor)
    #     self.assertEqual(expected_result, actual_results)
    #
    # def sample_test_3(self):
    #     solution = Solution()
    #     dividend = 18
    #     divisor = 3
    #     expected_result = 6
    #     actual_results = solution.divide(dividend, divisor)
    #     self.assertEqual(expected_result, actual_results)

    def sample_test_4(self):
        solution = Solution()
        dividend = -1
        divisor = 1
        expected_result = -1
        actual_results = solution.divide(dividend, divisor)
        self.assertEqual(expected_result, actual_results)

if __name__ == '__main__':
    unittest.main()
