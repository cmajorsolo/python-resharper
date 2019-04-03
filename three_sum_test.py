import unittest
from three_sum import Solution

class threeSumTest(unittest.TestCase):
    def test_sample_case(self):
        input = [-1, 0, 1, 2, -1, -4]
        expectedResult = [[-1, 0, 1], [-1, -1, 2]]
        solution = Solution()
        actualResult = solution.threeSum2(input)
        self.assertEqual(expectedResult, actualResult)


if __name__ == '__main__':
    unittest.main()