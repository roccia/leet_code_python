class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


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

    def add_two_numbers(self,l1,l2):
        pass

a = ListNode(2)
a.next = ListNode(4)
a.next.next = ListNode(3)
a.next.next.next = ListNode(5)
print(a.val, a.next.val, a.next.next.val)

b = ListNode(5)
b.next = ListNode(6)
b.next.next = ListNode(4)
print(b.val, b.next.val, b.next.next.val)

re = Solution().addTwoNumbers(a, b)
print(re.val, re.next.val, re.next.next.val)
