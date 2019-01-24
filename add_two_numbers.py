from list_node import ListNode

class addTwoNumbers:
    passToNext = 0
    def addTwoNumbersSolution(self, l1, l2):
        return self.getSum(l1, l2)

    def getSum(self, l1, l2):
        if self.passToNext == 0:
            sum = l1.val + l2.val
        elif self.passToNext == 1:
            sum = l1.val + l2.val + 1

        if sum >= 10:
            final_result = sum - 10
            self.passToNext = 1
        else:
            final_result = sum
            self.passToNext = 0

        result_node = ListNode(final_result)
        if(l1.next is not None and l2.next is not None):
            result_node.next = self.getSum(l1.next, l2.next)
        elif(l1.next is not None and l2.next is None):
            tempNode = ListNode(0)
            result_node.next = self.getSum(l1.next, tempNode)
        elif(l1.next is None and l2.next is not None):
            tempNode = ListNode(0)
            result_node.next = self.getSum(tempNode, l2.next)
        else:
            if self.passToNext == 1:
                result_node.next = ListNode(1)
            else:
                result_node.next = None

        return result_node

    def toList(self, node, resultList):
        resultList.append(node.val)
        if (node.next is not None):
            self.toList(node.next, resultList)
        return resultList

    def depthOfList(self, node, depth=1):
        if node.next is not None:
            depth = self.depthOfList(node.next, depth) + 1
        return depth


