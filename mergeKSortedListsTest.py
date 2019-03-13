import unittest
from mergeKSortedLists import Solution
from ListNode import ListNode

class mergeKSortedListTest(unittest.TestCase):
    def example_test(self):
        item1node1 = ListNode(1)
        item1node2 = ListNode(4)
        item1node3 = ListNode(5)
        item1node1.next = item1node2
        item1node2.next = item1node3

        item2Node1 = ListNode(1)
        item2Node2 = ListNode(3)
        item2Node3 = ListNode(4)
        item2Node1.next = item2Node2
        item2Node2.next = item2Node3

        item3Node1 = ListNode(2)
        item3Node2 = ListNode(6)
        item3Node1.next = item3Node2

        inputList = [item1node1, item2Node1, item3Node1]

        outputNode1 = ListNode(1)
        outputNode2 = ListNode(1)
        outputNode3 = ListNode(2)
        outputNode4 = ListNode(3)
        outputNode5 = ListNode(4)
        outputNode6 = ListNode(4)
        outputNode7 = ListNode(5)
        outputNode8 = ListNode(6)
        outputNode1.next = outputNode2
        outputNode2.next = outputNode3
        outputNode3.next = outputNode4
        outputNode4.next = outputNode5
        outputNode5.next = outputNode6
        outputNode6.next = outputNode7
        outputNode7.next = outputNode8

        solution = Solution()
        # actualResult = solution.mergeKLists(inputList)
        actualResult = solution.mergeKListsWithPriorityQueue(inputList)
        compareResult = outputNode1.equalTo(actualResult)
        self.assertTrue(compareResult)


if __name__ == '__main__':
    unittest.main()
