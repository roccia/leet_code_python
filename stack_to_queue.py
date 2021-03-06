# 两个栈实现队列
# 入队：元素进栈A
# 出队：先判断栈B是否为空，为空则将栈A中的元素pop出来并push进栈B，
# 再将栈B的第一个元素pop出栈，如不为空则直接从栈B中pop第一个元素出栈
# 这样做入队的复杂度为O(1)，出队的复杂度则变为O(n)


class Queue:
    def __init__(self):
        self.stackA = []
        self.stackB = []

    def push(self, element):
        self.stackA.append(element)

    def pop(self):
        if not self.stackA:
            return None
        if not self.stackB:
            for i in range(len(self.stackA)):
                self.stackB.append(self.stackA.pop())

        return self.stackB.pop()

q = Queue()
q.push(1)
q.pop()

q.push(2)

print(q.__dict__)

# 进栈：元素入队A
#
# 出栈：判断如果队A只有一个元素，则直接出队。否则，把队A中的元素出队并入队B，直到队A中只有一个元素，再直接出队。
#
# 分析：直接用python的list实现栈，以list尾为栈首，则出栈和进栈的复杂度都为O(1)。而用两个队列实现栈，因为进栈要用insert，
# 因此复杂度为O(n)；出栈复杂度为O(n^2)，因为需要连续insert。


class Stack:
    def __init__(self):
        self.queueA = []
        self.queueB = []

    def push(self, element):
        self.queueA.insert(0, element)

    def pop(self):
        if not self.queueA:
            return None
        while len(self.queueA) != 1:
            self.queueB.insert(0, self.queueA.pop())
        self.queueA, self.queueB = self.queueB, self.queueA
        return self.queueB.pop()

s = Stack()
s.push(1)
s.push(2)
s.pop()
print(s.__dict__)


class Stack1:
    def __init__(self):
        self.stack = []
    def add(self,val):
        if val not in self.stack:
            self.stack.append(val)
            return True
        return False

    def peek(self):
        return self.stack[0]

    def remove(self):
        if len(self.stack) <= 0:
            return 'No element'
        else:
            return self.stack.pop()

class Queue1:
    def __init__(self):
        self.queue = list()

    def add_to_top(self,val):
        if val not in self.queue:
            self.queue.insert(0,val)
            return True
        return False

    def size(self):
        return len(self.queue)

    def remove(self):
        if len(self.queue) > 0 :
            return self.queue.pop()
        return 'No element'
