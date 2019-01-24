import unittest
from string_to_integer import Solution

class reverse_integer_test(unittest.TestCase):
    def reverse_integer_function_test(self):
        testString = "42"
        expectedResult = 42
        solution = Solution()
        result = solution.myAtoi(testString)
        self.assertEqual(expectedResult, result)

    def reverse_integer_function_test_2(self):
        testString = "   -42"
        expectedResult = -42
        solution = Solution()
        result = solution.myAtoi(testString)
        self.assertEqual(expectedResult, result)

    def reverse_integer_function_test_3(self):
        testString = "4193 with words"
        expectedResult = 4193
        solution = Solution()
        result = solution.myAtoi(testString)
        self.assertEqual(expectedResult, result)

    def reverse_integer_function_test_4(self):
        testString = "words and 987"
        expectedResult = 0
        solution = Solution()
        result = solution.myAtoi(testString)
        self.assertEqual(expectedResult, result)

    def reverse_integer_function_test_5(self):
        testString = "-91283472332"
        expectedResult = -2147483648
        solution = Solution()
        result = solution.myAtoi(testString)
        self.assertEqual(expectedResult, result)

    def reverse_integer_function_test_6(self):
        testString = "3.1415"
        expectedResult = 3
        solution = Solution()
        result = solution.myAtoi(testString)
        self.assertEqual(expectedResult, result)

    def reverse_integer_function_test_7(self):
        testString = "00000000000001234"
        expectedResult = 1234
        solution = Solution()
        result = solution.myAtoi(testString)
        self.assertEqual(expectedResult, result)

    def reverse_integer_function_test_8(self):
        testString = "  -0012a42"
        expectedResult = -12
        solution = Solution()
        result = solution.myAtoi(testString)
        self.assertEqual(expectedResult, result)

    def reverse_integer_function_test_9(self):
        testString = "   +0 123"
        expectResult = 0
        solution = Solution()
        result = solution.myAtoi(testString)
        self.assertEqual(expectResult, result)

    def reverse_integer_function_test_10(self):
        testString = "-   234"
        expectResult = 0
        solution = Solution()
        result = solution.myAtoi(testString)
        self.assertEqual(expectResult, result)

    def test_11(self):
        testString = "0-1"
        expectResult = 0
        solution = Solution()
        result = solution.myAtoi(testString)
        self.assertEqual(expectResult, result)

    def test_12(self):
        testString = "-5-"
        expectResult = -5
        solution = Solution()
        result = solution.myAtoi(testString)
        self.assertEqual(expectResult, result)

    def test_13(self):
        testString = "123-"
        expectResult = 123
        solution = Solution()
        result = solution.myAtoi(testString)
        self.assertEqual(expectResult, result)

    def test_13(self):
        testString = "      -11919730356x"
        expectResult = -2147483648
        solution = Solution()
        result = solution.myAtoi(testString)
        self.assertEqual(expectResult, result)






