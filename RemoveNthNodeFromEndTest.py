import unittest
from ListNode import ListNode
from RemoveNthNodeFromEnd import Solution


class RemoveNthNodeFromEndTest(unittest.TestCase):
    def example_test(self):
        node1 = ListNode(1)
        node2 = ListNode(2)
        node3 = ListNode(3)
        node4 = ListNode(4)
        node5 = ListNode(5)
        node1.next = node2
        node2.next = node3
        node3.next = node4
        node4.next = node5

        node1ToReturn = ListNode(1)
        node2ToReturn = ListNode(2)
        node3ToReturn = ListNode(3)
        node5ToReturn = ListNode(5)
        node1ToReturn.next = node2ToReturn
        node2ToReturn.next = node3ToReturn
        node3ToReturn.next = node5ToReturn
        solution = Solution()
        expectedOutputNode = solution.removeNthFromEnd(node1, 2)
        actualOutputNode = node1ToReturn
        compareResult = actualOutputNode.equalTo(expectedOutputNode)
        self.assertEqual(compareResult, True)

    def shortList_test(self):
        node1 = ListNode(1)
        node2 = ListNode(2)
        node1.next = node2
        nodeToReturn = ListNode(2)
        solution = Solution()
        expectedOutputNode = solution.removeNthFromEnd(node1, 2)
        actualOutputNode = nodeToReturn
        compareResult = actualOutputNode.equalTo(expectedOutputNode)
        self.assertEqual(compareResult, True)

    def oneNode_test(self):
        node1 = ListNode(1)
        solution = Solution()
        expectedOutputNode = solution.removeNthFromEnd(node1, 1)
        self.assertIsNone(expectedOutputNode)


if __name__ == '__main__':
    unittest.main()


