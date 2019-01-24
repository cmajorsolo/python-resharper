import math

class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        if len(nums1) == len(nums2) == 0:
            return 0.0
        result = self.zip_up_all(nums1, nums2)
        result = sorted(result)
        oddLenght = len(result) % 2
        medianIndex = math.floor(len(result) / 2)
        if oddLenght > 0:
            median = result[medianIndex]
        else:
            median = (result[medianIndex] + result[medianIndex - 1]) / 2
        print(result)
        print(median)
        return median

    def zip_up_all(self, nums1, nums2):
        if len(nums1) > len(nums2):
            celling = len(nums2)
            result = self.zip_two_nums(nums1, nums2, celling)
            result.extend(nums1[celling:])
        elif len(nums2) > len(nums1):
            celling = len(nums1)
            result = self.zip_two_nums(nums1, nums2, celling)
            result.extend(nums2[celling:])
        else:
            result = self.zip_two_nums(nums1, nums2, len(nums1))

        return result

    def zip_two_nums(self, nums1, nums2, celling):
        result = []
        for i in range (0, celling):
            result.append(nums1[i])
            result.append(nums2[i])
        return result
