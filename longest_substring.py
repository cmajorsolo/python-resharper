from collections import deque

class findLongestSubString:


    def longest_string_online(self, s):
        curr = deque()
        longest = 0
        for c in s:
            if c in curr:
                while curr.popleft() != c: pass
            curr.append(c)
            longest = max(longest, len(curr))
        return max(len(curr), longest)