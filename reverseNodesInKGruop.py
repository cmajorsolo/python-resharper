from ListNode import ListNode

class Solution:
    def swapInKGruop(self, head, k):
        kPointer = k
        start = cur = pointer = ListNode(0)
        pointer.next = head

        while pointer.next:
            stack = []
            while kPointer > 0:
                if pointer.next:
                    stack.append(pointer.next)
                    pointer = pointer.next
                kPointer -= 1

            if len(stack) >= k:
                while stack:
                    node = stack.pop()
                    cur.next = ListNode(node.val)
                    cur = cur.next
            else:
                while stack:
                    node = stack.pop(0)
                    cur.next = ListNode(node.val)
                    cur = cur.next
            kPointer = k
        return start.next