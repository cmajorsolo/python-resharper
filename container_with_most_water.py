class Solution:
    def maxAreaBrutalForce(self, height):
        result = -1
        if len(height) == 1 or len(height) == 0:
            return 0
        elif len(height) == 2:
            return min(int(height[0]), int(height[1]))

        for i in range(0, len(height)):
            for j in range(1, len(height)):
                indexDifference = j - i
                heights = [height[i], height[j]]
                minHeight = min(heights)
                containerSize = indexDifference * minHeight
                if containerSize >= result:
                    result = containerSize
                j += 1
            i += 1
        print(result)

        return result

    def maxAreaPointers(self, height):
        if len(height) < 2:
            return 0
        result = -1
        l = 0
        r = len(height) - 1
        while l < r:
            area = min([height[l], height[r]]) * (r - l)
            result = max(result, area)
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        return result