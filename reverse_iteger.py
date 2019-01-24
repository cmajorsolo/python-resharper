import math
class Solution:
    def reverseInteger(self, x):
        rev = 0
        max = 2147483647
        # min = -2147483647
        prefix = 0
        while x is not 0:
            if x < 0:
                prefix = -1
                x = abs(x)
            pop = x % 10
            x = math.floor(x / 10)
            if rev > max / 10 or (rev == max / 10 and pop > 7):
                return 0
            # if rev < min / 10 or (rev == min / 10 and pop < -8):
            #     return 0
            rev = rev * 10 + pop
        if prefix is -1:
            rev = -rev
        return rev
