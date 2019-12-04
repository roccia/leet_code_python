class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None
ss`

class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """

        ans = ListNode(0)  # 新建一个节点，初始值为0
        temp = ans
        tempsum = 0

        while True:
            if l1 is not None:
                tempsum += l1.val  # l1链表节点值添加到总和里
                l1 = l1.next  # 指针指向下一个节点
            if l2 is not None:
                tempsum += l2.val  # l2链表节点值添加到总和里
                l2 = l2.next  # 指针指向下一个节点

            temp.val = tempsum % 10  # 取余数（满十进位），赋值当前节点值

            tempsum = int(tempsum / 10)  # 获取进位数赋值给总和（比如tempsum为10则进1位，否则进位为0），下一次节点相加，从新的总和开始。
            print('####')
            print(tempsum)
            if l1 is None and l2 is None and tempsum == 0:  # 直到没有进位了，同时节点位空了，跳出循环。（这里加上tempsum==0条件是因为，最后两个节
                break  # 点和值可能大于10）

            temp.next = ListNode(0)  # 新建下一个节点，存放和
            temp = temp.next  # 指针指向下一个节点

        return ans

    def add_two_numbers(self, l1, l2):
        len1, len2 = self.get_length(l1), self.get_length(l2)
        l1 = self.add_zero(len2 - len1, l1)
        l2 = self.add_zero(len1 - len2, l2)
        temp, ans = self.combine_list(l1, l2)
        if temp > 0:
            l3 = ListNode(temp)
            l3.next = ans
            ans = l3
        return ans

    def get_length(self, node):
        length = 0
        while node:
            length += 1
            node = node.next
        return length

    def add_zero(self, n, node):
        for i in range(n):
            new_list = ListNode(0)
            new_list.next = node
            node = new_list
        return node

    def combine_list(self, l1, l2):
        if not l1 and not l2:
            return 0, None
        temp, new_list = self.combine_list(l1.next, l2.next)
        temp_sum = l1.val + l2.val
        ans = ListNode(temp_sum % 10)
        ans.next = new_list
        return temp_sum // 10, ans


a = ListNode(2)
a.next = ListNode(4)
a.next.next = ListNode(3)
#a.next.next.next = ListNode(5)

print(a.val, a.next.val, a.next.next.val)

b = ListNode(5)
b.next = ListNode(6)
b.next.next = ListNode(4)
print(b.val, b.next.val, b.next.next.val)

res = Solution().add_two_numbers(a, b)

# re = Solution().addTwoNumbers(a, b)
print(res.val, res.next.val, res.next.next.val)
