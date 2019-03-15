import unittest
from ListNode import ListNode
from reverseNodesInKGruop import Solution

class reverseNodeInKGroupTest(unittest.TestCase):
    def example_k_is_3_test(self):
        node1 = ListNode(1)
        node2 = ListNode(2)
        node3 = ListNode(3)
        node4 = ListNode(4)
        node5 = ListNode(5)
        node1.next = node2
        node2.next = node3
        node3.next = node4
        node4.next = node5

        k = 3

        expectedNode1 = ListNode(3)
        expectedNode2 = ListNode(2)
        expectedNode3 = ListNode(1)
        expectedNode4 = ListNode(4)
        expectedNode5 = ListNode(5)
        expectedNode1.next = expectedNode2
        expectedNode2.next = expectedNode3
        expectedNode3.next = expectedNode4
        expectedNode4.next = expectedNode5

        solution = Solution()
        actualResult = solution.swapInKGruop(node1, k)
        self.assertTrue(expectedNode1.equalTo(actualResult))

    def example_k_is_2_test(self):
        node1 = ListNode(1)
        node2 = ListNode(2)
        node3 = ListNode(3)
        node4 = ListNode(4)
        node5 = ListNode(5)
        node1.next = node2
        node2.next = node3
        node3.next = node4
        node4.next = node5

        k = 2

        expectedNode1 = ListNode(2)
        expectedNode2 = ListNode(1)
        expectedNode3 = ListNode(4)
        expectedNode4 = ListNode(3)
        expectedNode5 = ListNode(5)
        expectedNode1.next = expectedNode2
        expectedNode2.next = expectedNode3
        expectedNode3.next = expectedNode4
        expectedNode4.next = expectedNode5

        solution = Solution()
        actualResult = solution.swapInKGruop(node1, k)
        self.assertTrue(expectedNode1.equalTo(actualResult))

    def more_than_2_groups_test(self):
        node1 = ListNode(1)
        node2 = ListNode(2)
        node3 = ListNode(3)
        node4 = ListNode(4)
        node5 = ListNode(5)
        node6 = ListNode(6)
        node1.next = node2
        node2.next = node3
        node3.next = node4
        node4.next = node5
        node5.next = node6

        k = 3

        expectedNode1 = ListNode(3)
        expectedNode2 = ListNode(2)
        expectedNode3 = ListNode(1)
        expectedNode4 = ListNode(6)
        expectedNode5 = ListNode(5)
        expectedNode6 = ListNode(4)
        expectedNode1.next = expectedNode2
        expectedNode2.next = expectedNode3
        expectedNode3.next = expectedNode4
        expectedNode4.next = expectedNode5
        expectedNode5.next = expectedNode6

        solution = Solution()
        actualResult = solution.swapInKGruop(node1, k)
        self.assertTrue(expectedNode1.equalTo(actualResult))

    def more_than_2_gruops_one_node_left_test(self):
        node1 = ListNode(1)
        node2 = ListNode(2)
        node3 = ListNode(3)
        node4 = ListNode(4)
        node5 = ListNode(5)
        node6 = ListNode(6)
        node7 = ListNode(7)
        node1.next = node2
        node2.next = node3
        node3.next = node4
        node4.next = node5
        node5.next = node6
        node6.next = node7

        k = 3

        expectedNode1 = ListNode(3)
        expectedNode2 = ListNode(2)
        expectedNode3 = ListNode(1)
        expectedNode4 = ListNode(6)
        expectedNode5 = ListNode(5)
        expectedNode6 = ListNode(4)
        expectedNode7 = ListNode(7)
        expectedNode1.next = expectedNode2
        expectedNode2.next = expectedNode3
        expectedNode3.next = expectedNode4
        expectedNode4.next = expectedNode5
        expectedNode5.next = expectedNode6
        expectedNode6.next = expectedNode7

        solution = Solution()
        actualResult = solution.swapInKGruop(node1, k)
        self.assertTrue(expectedNode1.equalTo(actualResult))


if __name__ == '__main__':
    unittest.main()
