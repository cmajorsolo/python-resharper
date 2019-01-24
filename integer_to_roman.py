from collections import defaultdict

class Solution:
    numbersDictionary = {
        1: "I",
        5: "V",
        10: "X",
        50: "L",
        100: "C",
        500: "D",
        1000: "M",
        4: "IV",
        9: "IX",
        40: "XL",
        90: "XC",
        400: "CD",
        900: "CM"
    }
    defaultNumbersDictionary = defaultdict(lambda: -1, numbersDictionary)

    def intToRoman(self, num):
        result = ""
        result = self.process(num, result)
        return result

    def process(self, num, result):
        calcResult = self.getSubRoman(num)
        if isinstance(calcResult[1], str):
            result += calcResult[1]
        elif isinstance(calcResult[1], int):
            for i in range(0, calcResult[1]):
                result += self.defaultNumbersDictionary[calcResult[0]]

        if calcResult[2] != 0:
            result = self.process(calcResult[2], result)
            return result
        else:
            return result

    def getSubRoman(self, num):
        divideFactor = 0
        if self.defaultNumbersDictionary[num] == -1:
            if 1 <= num < 4:
                divideFactor = 1
            elif 4 < num < 9:
                divideFactor = 5
            elif num > 10 and num < 40:
                divideFactor = 10
            elif num > 40 and num < 50:
                divideFactor = 40
            elif num > 50 and num < 90:
                divideFactor = 50
            elif num > 90 and num < 100:
                divideFactor = 90
            elif num > 100 and num < 400:
                divideFactor = 100
            elif num > 400 and num < 500:
                divideFactor = 400
            elif num > 500 and num < 900:
                divideFactor = 500
            elif num > 900 and num < 1000:
                divideFactor = 900
            elif num > 1000 and num <= 3999:
                divideFactor = 1000
            result, remaining = divmod(num, divideFactor)
            return [divideFactor, result, remaining]
        else:
            remaining = 0
            return [divideFactor, self.defaultNumbersDictionary[num], remaining]





