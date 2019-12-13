# WIP

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def __init__(self, pos):
        self.size = 0
        self.pos = pos

    def hasCycle(self, head: ListNode) -> bool:
        while head is not None:
            self.size = self.size + 1
            head = head.next
        if self.size - 1 > self.pos >= 0:
            return True
        else:
            return False


if __name__ == '__main__':
    inputArray = input()
    pos = int(input())

    firstNode = None
    prevNode = None
    for item in inputArray:
        if prevNode is None:
            firstNode = ListNode(item)
            prevNode = firstNode
        else:
            node = ListNode(item)
            prevNode.next = node
            prevNode = node

    solution = Solution(pos)
    print(solution.hasCycle(firstNode))
