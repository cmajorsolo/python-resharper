import math

class Solution:
    def longestPalindrome2(self, string):
        maxLength = 1
        start = 0
        length = len(string)

        for i in range(1, length):
            low = i - 1
            high = i
            while low >= 0 and high < length and string[low] == string[high]:
                if high - low + 1 > maxLength:
                    start = low
                    maxLength = high - low + 1
                low -= 1
                high += 1
            low = i - 1
            high = i + 1
            while low >= 0 and high < length and string[low] == string[high]:
                if high - low + 1 > maxLength:
                    start = low
                    maxLength = high - low + 1
                low -= 1
                high += 1
        print("longest panlindrome substring is: ")
        print(string[start:start + maxLength])
        return string[start:start + maxLength]

    def longestPalindrome3(self, string):
        n = len(string)
        table = [[0 for x in range(n)] for y in range(n)]
        maxLength = 1
        i = 0
        while (i < n):
            table[i][i] = True
            i = i + 1

        start = 0
        i = 0
        while i < n -1 :
            if (string[i] == string[i + 1]):
                table[i][i+1] = True
                start = i
                maxLength = 2
            i = i + 1

        k = 3
        while k <= n:
            i = 0
            while i < (n - k + 1):
                j = i + k - 1
                if (table[i + 1][j - 1]) and string[i] == string[j]:
                    table[i][j] = True

                    if (k > maxLength):
                        start = i
                        maxLength = k
                i = i + 1
            k = k + 1


        # print(table)
        # print(string[start: start + maxLength])
        return string[start: start + maxLength]

    def longestPalindromeBrutalForce(self, string):
        i = 0
        length = 0
        while i < len(string):
            j = i + 1
            while j <= len(string):
                # print(string[i: j])
                panlindorme = self.ifPanlinrome(string[i:j])
                # print(panlindorme)
                if panlindorme[0] is True:
                    if panlindorme[1] > length:
                        length = panlindorme[1]
                        longestPanlindrome = string[i:j]

                j += 1
            i += 1
            # print(length, longestPanlindrome)
        return longestPanlindrome

    def ifPalinrome(self, string):
        if len(string) == 1:
            return True, 1
        elif len(string) % 2 != 0:
            middleIndex = math.floor(len(string)/2)
            lowerIndex = middleIndex - 1
            upperIndex = middleIndex + 1
        elif len(string) % 2 == 0:
            lowerIndex = int(len(string) / 2 - 1)
            upperIndex = int(len(string) / 2)

        while lowerIndex >= 0 and upperIndex <= len(string):
            if string[lowerIndex] != string[upperIndex]:
                return False, 0
            lowerIndex -= 1
            upperIndex += 1
            
        return True, len(string)

    def longestPalindrome(self, s):
        start = 0
        end = 0
        for i in range(0, len(s)):
            len1 = self.expandAroundCenter(s, i, i)
            len2 = self.expandAroundCenter(s, i, i+1)
            length = max(len1, len2)
            if(length > end - start):
                start = math.ceil(i - (length - 1) / 2)
                end = int(i + length / 2)
        return s[start: end+1]

    def expandAroundCenter(self, s, start, end):
        while start >= 0 and end < len(s) and s[start] == s[end]:
            start -= 1
            end += 1
        return end - start - 1



