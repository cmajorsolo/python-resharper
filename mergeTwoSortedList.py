from ListNode import ListNode

class Solution:
    def mergeTwoLists(self, l1Node1, l2Node1):
        # l1Node1Next, l2Node1Next = self.swapNext(l1Node1, l2Node1)
        # while l1Node1Next is not None or l2Node1Next is not None:
        #     l1Node1Next, l2Node1Next = self.swapNext(l1Node1Next, l2Node1Next)
        #
        # return l1Node1
        newList = ListNode(0)
        cur = newList
        while l1Node1 and l2Node1:
            if l1Node1.val < l2Node1.val:
                cur.next = l1Node1
                l1Node1 = l1Node1.next
            else:
                cur.next = l2Node1
                l2Node1 = l2Node1.next
            cur = cur.next
        cur.next = l1Node1 or l2Node1
        return newList.next
