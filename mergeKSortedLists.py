from ListNode import ListNode
from queue import PriorityQueue

class Solution:
    def mergeKLists(self, nodeList):
        if len(nodeList) is 0:
            return []
        else:
            for index, item in enumerate(nodeList):
                if index == 0:
                    start = item
                    tmp = start
                elif index == 1:
                    tmp = self.merge2SortedList(start, item)
                else:
                    tmp = self.merge2SortedList(tmp, item)
            return tmp

    def merge2SortedList(self, l1node1, l2node1):
        result = ListNode(0)
        cur = result
        while l1node1 and l2node1:
            if l1node1.val < l2node1.val:
                cur.next = l1node1
                l1node1 = l1node1.next
            else:
                cur.next = l2node1
                l2node1 = l2node1.next
            cur = cur.next
        cur.next = l1node1 or l2node1
        return result.next

    def mergeKListsWithPriorityQueue(self, lists):
        head = ListNode(0)
        cur = head
        q = PriorityQueue()
        for item in lists:
            if item:
                q.put((item.val, item))
        while not q.empty():
            val, node = q.get()
            cur.next = ListNode(val)
            cur = cur.next
            node = node.next
            if node:
                q.put((node.val, node))
        return head.next


