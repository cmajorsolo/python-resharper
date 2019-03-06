import unittest
from validParentheses import Solution

class validParenthesesTest(unittest.TestCase):
    def example_test(self):
        inputString = "()"
        solution = Solution()
        self.assertTrue(solution.isValied(inputString))

    def nestedExample_test(self):
        inputString = "{[]}"
        solution = Solution()
        self.assertTrue(solution.isValied(inputString))

    def falseExample_test(self):
        inputString = "([)]"
        solution = Solution()
        self.assertFalse(solution.isValied(inputString))