class Solution:
    def threeSum(self, nums):
        result = []
        print(float('inf'))
        for i in range(0, len(nums)):
            for j in range(i+1, len(nums)):
                for k in range(j+1, len(nums)):
                    if nums[i] + nums[j] + nums[k] == 0:
                        childResult = [nums[i], nums[j], nums[k]]
                        childResult = sorted(childResult)
                        if (childResult not in result):
                            result.append(childResult)
        return result

    def threeSum2(self, nums):
        nums = sorted(nums)
        ans = []
        target = float('inf')
        for i in range(len(nums)):
            if -nums[i] == target:
                continue
            target = -nums[i]
            l, r = i + 1, len(nums) - 1
            fl, fr = float('inf'), float('inf')
            while l < r:
                if nums[l] + nums[r] == target:
                    if fl != nums[l] or fr != nums[r]:
                        ans.append([-target, nums[l], nums[r]])
                        fl, fr = nums[l], nums[r]
                    r -= 1
                elif nums[l] + nums[r] < target:
                    l += 1
                else:
                    r -= 1
        return ans

