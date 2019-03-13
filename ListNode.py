class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

    def equalTo(self, node2):
        # same length
        # check if same list of values
        node1Next = self.next
        lengthCounter1 = 1
        if node1Next is None:
            node1ValList = [self.val]
        else:
            node1ValList = [self.val, node1Next.val]
            while node1Next.next is not None:
                node1Next = node1Next.next
                node1ValList.append(node1Next.val)
                lengthCounter1 += 1

        node2Next = node2.next
        lengthCounter2 = 1
        if node2Next is None:
            node2ValList = [self.val]
        else:
            node2ValList = [node2.val, node2Next.val]
            while node2Next.next is not None:
                node2Next = node2Next.next
                node2ValList.append(node2Next.val)
                lengthCounter2 += 1

        if lengthCounter1 != lengthCounter2:
            return False
        else:
            for index, val in enumerate(node1ValList):
                if node2ValList[index] != val:
                    return False

            return True

    def __lt__(self, other):
        return self.val < other.val

    def __eq__(self, other):
        return self.val == other.val

