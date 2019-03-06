from ListNode import ListNode

class Solution(object):
    node1 = ListNode(1)
    node2 = ListNode(2)
    node3 = ListNode(3)
    node4 = ListNode(4)
    node5 = ListNode(5)
    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node5

    def removeNthFromEnd(self, head, n):
        if head.next is None:
            return None
        else:
            headLength = 2
            headNext = head.next
            headList = [head, headNext]
            while headNext.next is not None:
                headNext = headNext.next
                headList.append(headNext)
                headLength += 1

            indexToRemove = headLength - n

            if indexToRemove > headLength - 1 or indexToRemove < 0:
                raise Exception("Index out of range")
            else:
                del headList[indexToRemove]
                if indexToRemove == 0:
                    pass
                elif indexToRemove != len(headList):
                    headList[indexToRemove-1].next = headList[indexToRemove]
                else:
                    headList[indexToRemove - 1].next = None
                return headList[0]