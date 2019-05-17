import  unittest
from implement_strStr import Solution


class implement_strStr_Test(unittest.TestCase):
    def test_example_1(self):
        solution = Solution()
        intput_string = 'hello'
        needle = 'll'
        expected_output = 2
        actual_output = solution.strStr(intput_string, needle)
        self.assertEqual(expected_output, actual_output)

    def test_example_2(self):
        solution = Solution()
        intput_string = 'aaaaa'
        needle = 'bba'
        expected_output = -1
        actual_output = solution.strStr(intput_string, needle)
        self.assertEqual(expected_output, actual_output)

    def test_example_3(self):
        solution = Solution()
        intput_string = 'aaa'
        needle = 'aaaaa'
        expected_output = -1
        actual_output = solution.strStr(intput_string, needle)
        self.assertEqual(expected_output, actual_output)

    def test_example_4(self):
        solution = Solution()
        intput_string = 'aaa'
        needle = 'aaa'
        expected_output = 0
        actual_output = solution.strStr(intput_string, needle)
        self.assertEqual(expected_output, actual_output)

    def test_example_5(self):
        solution = Solution()
        intput_string = 'mississippi'
        needle = 'pi'
        expected_output = 9
        actual_output = solution.strStr(intput_string, needle)
        self.assertEqual(expected_output, actual_output)


if __name__ == '__main__':
    unittest.main()
