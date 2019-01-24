import unittest
from twoSum import TwoSum

class SumTest(unittest.TestCase):
    def test_sum_two(self):
        twoSumInstance = TwoSum()
        self.assertEqual(twoSumInstance.twoSum([2,7,11,15], 13), [0, 2])

    def test_sum_two_case2(self):
        twoSumInstance = TwoSum()
        self.assertEqual(twoSumInstance.twoSum([3, 2, 4], 6), [1, 2])


if __name__ == '__main__':
    unittest.main()
