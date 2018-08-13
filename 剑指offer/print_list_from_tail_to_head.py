class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None


class Solution:
    # stack
    def print_list_from_tail_to_head(self, node):
        stack = []
        while node:
            stack.append(node.val)
            node.next
        while stack:
            print(stack.pop())

    # recursion
    def print_list_recursion(self, node):
        if node:
            self.print_list_recursion(node.next)
            print(node.val)

    def print_list(self, node):
        if not node:
            return []
        res = []
        head = node
        while head:
            res.insert(0, head.val)
            head = head.next
        return res
