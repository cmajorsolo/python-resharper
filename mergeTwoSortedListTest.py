import unittest
from mergeTwoSortedList import Solution
from ListNode import ListNode

class mergeTwoSortedList(unittest.TestCase):
    def twoSimpoleList_test(self):
        l1node1 = ListNode(1)
        l1node2 = ListNode(2)
        l1node3 = ListNode(4)
        l1node1.next = l1node2
        l1node2.next = l1node3
        l2node1 = ListNode(1)
        l2node2 = ListNode(3)
        l2node3 = ListNode(4)
        l2node1.next = l2node2
        l2node2.next = l2node3

        resultNode1 = ListNode(1)
        resultNode2 = ListNode(1)
        resultNode3 = ListNode(2)
        resultNode4 = ListNode(3)
        resultNode5 = ListNode(4)
        resultNode6 = ListNode(4)
        resultNode1.next = resultNode2
        resultNode2.next = resultNode3
        resultNode3.next = resultNode4
        resultNode4.next = resultNode5
        resultNode5.next = resultNode6

        solution = Solution()
        result = solution.mergeTwoLists(l1node1, l2node1)
        compareResult = resultNode1.equalTo(result)
        self.assertTrue(compareResult)

    def differerntLength_test(self):
        l1node1 = ListNode(1)
        l1node2 = ListNode(2)
        l1node1.next = l1node2
        l2node1 = ListNode(1)
        l2node2 = ListNode(3)
        l2node3 = ListNode(4)
        l2node1.next = l2node2
        l2node2.next = l2node3

        resultNode1 = ListNode(1)
        resultNode2 = ListNode(1)
        resultNode3 = ListNode(2)
        resultNode4 = ListNode(3)
        resultNode5 = ListNode(4)
        resultNode1.next = resultNode2
        resultNode2.next = resultNode3
        resultNode3.next = resultNode4
        resultNode4.next = resultNode5

        solution = Solution()
        result = solution.mergeTwoLists(l1node1, l2node1)
        compareResult = resultNode1.equalTo(result)
        self.assertTrue(compareResult)

    def oneNodeList_test(self):
        l1node1 = ListNode(1)
        l2node1 = ListNode(2)
        resultNode1 = ListNode(1)
        resultNode2 = ListNode(2)
        resultNode1.next = resultNode2

        solution = Solution()
        result = solution.mergeTwoLists(l1node1, l2node1)
        compareResult = resultNode1.equalTo(result)
        self.assertTrue(compareResult)

    def orderOfTwoLists_test(self):
        l1node1 = ListNode(1)
        l1node2 = ListNode(4)
        l1node1.next = l1node2
        l2node1 = ListNode(1)
        l2node2 = ListNode(3)
        l2node3 = ListNode(4)
        l2node1.next = l2node2
        l2node2.next = l2node3

        resultNode1 = ListNode(1)
        resultNode2 = ListNode(1)
        resultNode3 = ListNode(3)
        resultNode4 = ListNode(4)
        resultNode5 = ListNode(4)
        resultNode1.next = resultNode2
        resultNode2.next = resultNode3
        resultNode3.next = resultNode4
        resultNode4.next = resultNode5

        solution = Solution()
        result = solution.mergeTwoLists(l1node1, l2node1)
        compareResult = resultNode1.equalTo(result)
        self.assertTrue(compareResult)

    def orderOfTwoLists_test(self):
        l1node1 = ListNode(1)
        l1node2 = ListNode(3)
        l1node1.next = l1node2
        l2node1 = ListNode(5)
        l2node2 = ListNode(7)
        l2node3 = ListNode(9)
        l2node1.next = l2node2
        l2node2.next = l2node3

        resultNode1 = ListNode(1)
        resultNode2 = ListNode(3)
        resultNode3 = ListNode(5)
        resultNode4 = ListNode(7)
        resultNode5 = ListNode(9)
        resultNode1.next = resultNode2
        resultNode2.next = resultNode3
        resultNode3.next = resultNode4
        resultNode4.next = resultNode5

        solution = Solution()
        result = solution.mergeTwoLists(l1node1, l2node1)
        compareResult = resultNode1.equalTo(result)
        self.assertTrue(compareResult)

if __name__ == '__main__':
    unittest.main()
