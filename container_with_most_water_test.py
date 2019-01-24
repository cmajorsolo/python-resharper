import unittest
from container_with_most_water import Solution

class containerWithMostWaterTest(unittest.TestCase):
    def test_maxAreaBrutalForce(self):
        inputArray = [1,118,6,2,5,4,8,3,7]
        expectedResult = 49
        solution = Solution()
        actualResult = solution.maxAreaPointers(inputArray)
        self.assertEqual(actualResult, expectedResult)



