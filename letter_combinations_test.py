import unittest
from letter_combinations import Solution

class letter_combinations_test(unittest.TestCase):
    def simple_test(self):
        input = '23'
        expected_output = ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]
        solution = Solution()
        output = solution.letterCombinations(input)
        self.assertEqual(output, expected_output)

    def different_length_test(self):
        input = '237'
        expected_output = ["adp", "adq", "adr", "ads", "aep", "aeq", "aer", "aes",
                           "afp", "afq", "afr", "afs", "bdp", "bdq", "bdr", "bds",
                           "bep", "beq", "ber", "bes", "bfp", "bfq", "bfr", "bfs",
                           "cdp", "cdq", "cdr", "cds", "cep", "ceq", "cer", "ces",
                           "cfp", "cfq", "cfr", "cfs"]
        solution = Solution()
        output = solution.letterCombinations(input)
        self.assertEqual(output, expected_output)

if __name__ == '__main__':
    unittest.main()
