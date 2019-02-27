class Solution:
    def letterCombinations(self, digits):
        phone_numbers_dic = {'2': ['a', 'b', 'c'],
                             '3': ['d', 'e', 'f'],
                             '4': ['g', 'h', 'i'],
                             '5': ['j', 'k', 'l'],
                             '6': ['m', 'n', 'o'],
                             '7': ['p', 'q', 'r', 's'],
                             '8': ['t', 'u', 'v'],
                             '9': ['w', 'x', 'y', 'z']}
        result = []
        tmp = []
        for index, s in enumerate(digits):
            if index == 0:
                for item in phone_numbers_dic[s]:
                    result.append(item)
            else:
                for index, resultItem in enumerate(result):
                    for dicItem in phone_numbers_dic[s]:
                        tmpString = resultItem + dicItem
                        tmp.append(tmpString)
                result = tmp
                tmp = []
        return result