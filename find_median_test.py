import unittest
from find_median import Solution

class find_median_test(unittest.TestCase):
    def find_median_standard_test(self):
        nums1 = []
        nums2 = []
        finder = Solution()
        result = finder.findMedianSortedArrays(nums1, nums2)
        expected_result = 0.0
        self.assertEqual(result, expected_result)