import unittest
from remove_element import Solution

class RemoveElementTest(unittest.TestCase):
    # def example_test_1(self):
    #     nums = [3,2,2,3]
    #     val = 3
    #     expected_result = [2, 2]
    #     solution = Solution()
    #     actual_result = solution.removeElement(nums, val)
    #     self.assertEqual(expected_result, actual_result)

    def example_test_2(self):
        nums = [0, 1, 2, 2, 3, 0, 4, 2]
        val = 2
        expected_result = [0, 1, 3, 0, 4]
        solution = Solution()
        actual_result = solution.removeElement2(nums, val)
        self.assertEqual(expected_result, actual_result)


if __name__ == '__main__':
    unittest.main()
