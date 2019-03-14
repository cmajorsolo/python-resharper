from ListNode import ListNode

class Solution:
    def swapPairs(self, head):
        start = pointer = ListNode(0)
        while head and head.next:
            headNext = head.next
            tail = headNext.next

            pointer.next = ListNode(headNext.val)
            next = pointer.next
            next.next = ListNode(head.val)

            pointer = next.next
            head = tail

        if head and head.next is None:
            pointer.next = head

        return start.next
