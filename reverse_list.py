# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        current = head
        pre = None
        while current:
            next_node = current.next
            current.next = pre
            pre = current
            current = next_node
        head = pre
        return head

    def reverseBetewwn(self, head, m, n):
        if not head or m == n: return head
        p = dummy = ListNode(None)
        dummy.next = head
        for i in range(m - 1): p = p.next
        tail = p.next

        for i in range(n - m):
            tmp = p.next
            p.next = tail.next
            tail.next = tail.next.next
            p.next.next = tmp
        return dummy.next
