class Solution():
    def strStr(self, haystack, needle):
        needle_length = len(needle)
        if needle_length is 0:
            return 0
        else:
            for i in range(len(haystack)):
                # if i < len(haystack) - 2:
                end = i + needle_length
                if end > len(haystack):
                    return -1
                elif haystack[i:end] == needle:
                    return i
                # else:
                # if haystack[-needle_length] == needle:
                #     return i
            return -1
