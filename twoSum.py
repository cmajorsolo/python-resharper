class TwoSum:
    def twoSum(self, nums, target):
        for index, item in enumerate(nums):
            difference = target - item
            if (difference in nums):
                if (index != nums.index(difference)):
                    return [index, nums.index(difference)]

if __name__ == '__main__':
    # print([1,2,3].index(5))
    ts = TwoSum()
    ts.twoSum([3, 2, 4], 6)