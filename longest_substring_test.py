import unittest
from longest_substring import findLongestSubString

class find_longest_str_test(unittest.TestCase):
    def test_case_sample_value_ababa(self):
        test_string = 'twwkew'
        findLongestSubStringInstance = findLongestSubString()
        returnedResult = findLongestSubStringInstance.longest_string_online(test_string)
        # print(returnedResult)
        expectedResult = 3
        self.assertEqual(returnedResult, expectedResult)
