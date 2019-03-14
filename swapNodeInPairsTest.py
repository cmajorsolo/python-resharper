import unittest
from swapNodeInPairs import Solution
from ListNode import ListNode

class swapNodeInPairsTest(unittest.TestCase):
    def example_test(self):
        node1 = ListNode(1)
        node2 = ListNode(2)
        node3 = ListNode(3)
        node4 = ListNode(4)
        node1.next = node2
        node2.next = node3
        node3.next = node4

        resultNode1 = ListNode(2)
        resultNode2 = ListNode(1)
        resultNode3 = ListNode(4)
        resultNode4 = ListNode(3)
        resultNode1.next = resultNode2
        resultNode2.next = resultNode3
        resultNode3.next = resultNode4

        solution = Solution()
        actualResult = solution.swapPairs(node1)
        self.assertTrue(resultNode1.equalTo(actualResult))

    def odd_length_test(self):
        node1 = ListNode(1)
        node2 = ListNode(2)
        node3 = ListNode(3)
        node1.next = node2
        node2.next = node3

        resultNode1 = ListNode(2)
        resultNode2 = ListNode(1)
        resultNode3 = ListNode(3)
        resultNode1.next = resultNode2
        resultNode2.next = resultNode3
        solution = Solution()
        actualResult = solution.swapPairs(node1)
        self.assertTrue(resultNode1.equalTo(actualResult))

    def single_node_test(self):
        node1 = ListNode(1)
        expectedResult = node1

        solution = Solution()
        actualResult = solution.swapPairs(node1)
        self.assertTrue(expectedResult.equalTo(actualResult))

    def empty_test(self):
        node1 = ListNode(None)
        expectedResult = node1

        solution = Solution()
        actualResult = solution.swapPairs(node1)
        self.assertTrue(expectedResult.equalTo(actualResult))

if __name__ == '__main__':
    unittest.main()
