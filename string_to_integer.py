class Solution:
    def myAtoi(self, str):
        if len(str) is 0:
            return 0
        else:
            signed = ''
            result = ''
            for item in str:
                if item is ' ':
                    if len(result) != 0:
                        return self.getFinalResult(result, signed)
                    else:
                        if len(signed) != 0:
                            return 0
                        else:
                            pass
                elif item == '+' or item == '-':
                    if len(signed) is not 0:
                        if len(result) != 0:
                            return self.getFinalResult(result, signed)
                        else:
                            return 0
                    else:
                        if len(result) != 0:
                            return self.getFinalResult(result, signed)
                        else:
                            signed = item
                elif item in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
                    result += item
                elif item is '.':
                    if len(result) is 0:
                        return 0
                    else:
                        try:
                            finalResult = int(result)
                            if signed == '-':
                                finalResult = -finalResult
                            return finalResult
                        except ValueError:
                            return 0
                else:
                    if len(result) is 0:
                        return 0
                    else:
                        return self.getFinalResult(result, signed)

            try:
                finalResult = int(result)
                if signed == '-':
                    finalResult = -finalResult
            except ValueError:
                # print('got exception')
                # handle existing final result here
                return 0

            if finalResult > 2147483647:
                finalResult = 2147483647
            elif finalResult < -2147483648:
                finalResult = -2147483648

        return finalResult

    def getFinalResult(self, result, signed):
        try:
            finalResult = int(result)
            if signed == '-':
                finalResult = -finalResult

            if finalResult > 2147483647:
                finalResult = 2147483647
            elif finalResult < -2147483648:
                finalResult = -2147483648

            return finalResult
        except ValueError:
            return 0

