import unittest
from find_palindrome import Solution

class find_panlindrome_test(unittest.TestCase):
    def test_output(self):
        solution = Solution()
        actual_result = solution.longestPalindrome('babbad')
        expected_result = 'abba'
        self.assertEqual(actual_result, expected_result)

if __name__ == '__main__':
    unittest.main()
