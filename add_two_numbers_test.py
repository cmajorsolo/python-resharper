import unittest
from add_two_numbers import addTwoNumbers
from list_node import ListNode

class add_two_numbers_test(unittest.TestCase):
    def test_case_sample_value(self):
        addTwoNumbersInstance = addTwoNumbers()
        l1_3 = ListNode(3)
        l1_2 = ListNode(4)
        l1_2.next = l1_3
        l1_1 = ListNode(2)
        l1_1.next = l1_2
        l2_3 = ListNode(4)
        l2_2 = ListNode(6)
        l2_2.next = l2_3
        l2_1 = ListNode(5)
        l2_1.next = l2_2
        result_3 = ListNode(8)
        result_2 = ListNode(0)
        result_2.next = result_3
        result_1 = ListNode(7)
        result_1.next = result_2
        expected_result = [result_1.val, result_2.val, result_3.val]

        returned_result = addTwoNumbersInstance.addTwoNumbersSolution(l1_1, l2_1)
        # result = [returned_result.val]
        # result.append(returned_result.next.val)
        # result.append(returned_result.next.next.val)
        returned_result_list = addTwoNumbersInstance.toList(returned_result, [])
        print(returned_result_list)

        self.assertEqual(returned_result_list, expected_result)

    def test_case_with_one_more_digit_sum_result(self):
        addTwoNumbersInstance = addTwoNumbers()
        l1_3 = ListNode(6)
        l1_2 = ListNode(5)
        l1_2.next = l1_3
        l1_1 = ListNode(9)
        l1_1.next = l1_2
        l2_3 = ListNode(8)
        l2_2 = ListNode(4)
        l2_2.next = l2_3
        l2_1 = ListNode(9)
        l2_1.next = l2_2

        result_4 = ListNode(1)
        result_3 = ListNode(5)
        result_3.next = result_4
        result_2 = ListNode(0)
        result_2.next = result_3
        result_1 = ListNode(8)
        result_1.next = result_2
        expected_result = [result_1.val, result_2.val, result_3.val, result_4.val]

        returned_result = addTwoNumbersInstance.addTwoNumbersSolution(l1_1, l2_1)
        returned_result_list = addTwoNumbersInstance.toList(returned_result, [])

        print(returned_result_list)
        self.assertEqual(returned_result_list, expected_result)

    def test_case_with_different_length(self):
        addTwoNumbersInstance = addTwoNumbers()
        l1_3 = ListNode(1)
        l1_2 = ListNode(8)
        l1_2.next = l1_3
        l1_1 = ListNode(9)
        l1_1.next = l1_2
        l2_2 = ListNode(4)
        l2_1 = ListNode(9)
        l2_1.next = l2_2

        result_3 = ListNode(2)
        result_2 = ListNode(3)
        result_2.next = result_3
        result_1 = ListNode(8)
        result_1.next = result_2
        expected_result = [result_1.val, result_2.val, result_3.val]

        returned_result = addTwoNumbersInstance.addTwoNumbersSolution(l1_1, l2_1)
        returned_result_list = addTwoNumbersInstance.toList(returned_result, [])
        print(returned_result_list)
        self.assertEqual(returned_result_list, expected_result)

    def test_case_with_different_length_short_test(self):
        addTwoNumbersInstance = addTwoNumbers()
        l1_2 = ListNode(8)
        l1_1 = ListNode(1)
        l1_1.next = l1_2
        l2_1 = ListNode(0)

        result_2 = ListNode(8)
        result_1 = ListNode(1)
        result_1.next = result_2
        expected_result = [result_1.val, result_2.val]

        returned_result = addTwoNumbersInstance.addTwoNumbersSolution(l1_1, l2_1)
        returned_result_list = addTwoNumbersInstance.toList(returned_result, [])
        print(returned_result_list)
        self.assertEqual(returned_result_list, expected_result)

    def test_case_with_different_length_longer_test(self):
        addTwoNumbersInstance = addTwoNumbers()
        l1_4 = ListNode(2)
        l1_3 = ListNode(3)
        l1_3.next = l1_4
        l1_2 = ListNode(8)
        l1_2.next = l1_3
        l1_1 = ListNode(1)
        l1_1.next = l1_2
        l2_1 = ListNode(0)

        result_4 = ListNode(2)
        result_3 = ListNode(3)
        result_3.next = result_4
        result_2 = ListNode(8)
        result_2.next = result_3
        result_1 = ListNode(1)
        result_1.next = result_2

        expected_result = [result_1.val, result_2.val, result_3.val, result_4.val]

        returned_result = addTwoNumbersInstance.addTwoNumbersSolution(l1_1, l2_1)
        returned_result_list = addTwoNumbersInstance.toList(returned_result, [])
        print(returned_result_list)
        self.assertEqual(returned_result_list, expected_result)

if __name__ == '__main__':
    unittest.main()
