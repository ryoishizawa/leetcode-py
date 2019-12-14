# WIP

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        if head is None or head.next is None:
            return False
        slowNode = head
        fastNode = head.next
        while slowNode is not None:
            if fastNode is None or fastNode.next is None:
                return False
            if slowNode is fastNode:
                return True
            slowNode = slowNode.next
            fastNode = fastNode.next.next
        return True


