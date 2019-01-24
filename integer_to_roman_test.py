import unittest
from integer_to_roman import Solution

class integerToRomainTest(unittest.TestCase):
    def testInputSmallerThan4(self):
        input = 2
        expectedResult = 'II'
        solution = Solution()
        actualSolution = solution.intToRoman(input)
        self.assertEqual(expectedResult, actualSolution)

    def testInputEqualTo4(self):
        input = 4
        expectedResult = 'IV'
        solution = Solution()
        actualSolution = solution.intToRoman(input)
        self.assertEqual(expectedResult, actualSolution)

    def testInputEqualTo5(self):
        input = 5
        expectedResult = 'V'
        solution = Solution()
        actualSolution = solution.intToRoman(input)
        self.assertEqual(expectedResult, actualSolution)

    def testBiggerThan4SamllerThan10(self):
        input = 8
        expectedResult = 'VIII'
        solution = Solution()
        actualSolution = solution.intToRoman(input)
        self.assertEqual(expectedResult, actualSolution)

    def testInputEqualTo9(self):
        input = 9
        expectedResult = 'IX'
        solution = Solution()
        actualSolution = solution.intToRoman(input)
        self.assertEqual(expectedResult, actualSolution)

    def testInputEqualTo10(self):
        input = 10
        expectedResult = 'X'
        solution = Solution()
        actualSolution = solution.intToRoman(input)
        self.assertEqual(expectedResult, actualSolution)

    def testInputEqualTo100(self):
        input = 100
        expectedResult = 'C'
        solution = Solution()
        actualSolution = solution.intToRoman(input)
        self.assertEqual(expectedResult, actualSolution)

    def testInputEqualTo50(self):
        input = 50
        expectedResult = 'L'
        solution = Solution()
        actualSolution = solution.intToRoman(input)
        self.assertEqual(expectedResult, actualSolution)

    def testInputSmallerThan50(self):
        input = 20
        expectedResult = 'XX'
        solution = Solution()
        actualSolution = solution.intToRoman(input)
        self.assertEqual(expectedResult, actualSolution)

    def testInputSmallerThan50NotRound(self):
        input = 42
        expectedResult = "XLII"
        solution = Solution()
        actualSolution = solution.intToRoman(input)
        self.assertEqual(expectedResult, actualSolution)

    def testInputSmallerThan50NotRound2(self):
        input = 48
        expectedResult = "XLVIII"
        solution = Solution()
        actualSolution = solution.intToRoman(input)
        self.assertEqual(expectedResult, actualSolution)

    def testInputBiggerThan50(self):
        input = 61
        expectedResult = 'LXI'
        solution = Solution()
        actualSolution = solution.intToRoman(input)
        self.assertEqual(expectedResult, actualSolution)

    def testInputBiggerThan50RoundNumber(self):
        input = 80
        expectedResult = 'LXXX'
        solution = Solution()
        actualSolution = solution.intToRoman(input)
        self.assertEqual(expectedResult, actualSolution)

    def testInputBiggerThan50NotRoundNumber(self):
        input = 96
        expectedResult = "XCVI"
        solution = Solution()
        actualSolution = solution.intToRoman(input)
        self.assertEqual(expectedResult, actualSolution)
