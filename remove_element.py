class Solution:
    def removeElement(self, nums, val):
        x = curr = 0
        for index, value in enumerate(nums):
            if value != val:
                if x != curr:
                    nums[curr] = nums[x]
                    x += 1
                    curr += 1
                else:
                    x += 1
                    curr += 1
            elif value == val:
                x += 1

        return nums[:curr]

    def removeElement2(self, nums, val):
        offset = 0
        for i in range(len(nums)):
            print(i-offset, nums)
            if(nums[i-offset]==val):
                nums.remove(nums[i-offset])
                offset=offset+1
        return nums
