class Solution(object):
    def isValied(self, s):
        tmp = []
        if len(s) is 0:
            return True
        for char in s:
            if len(tmp) is 0:
                tmp.append(char)
            else:
                lastItem = tmp[-1]
                if char is ')' and lastItem is '(' \
                        or char is ']' and tmp[-1] is '[' \
                        or char is '}' and tmp[-1] is '{':
                    del tmp[-1]
                else:
                    tmp.append(char)
        if len(tmp) is 0:
            return True
        else:
            return False
