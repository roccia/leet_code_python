class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None


class Solution:
    def delete_node(self, head, node):
        if node == head:
            node = None

        if node.next is None:
            while head:
                if head.next == node:
                    head.next = None
                head = head.next
        else:
            node.val = node.next.val
            next_node = node.next
            node.next = next_node.next
            next_node = None
        return head
