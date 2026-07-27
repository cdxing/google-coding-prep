# LC 155 - Min Stack
#
# Design a stack that supports push, pop, top, and getMin in O(1) time.
#
# MinStack()       → initialize
# push(val)        → push val onto stack
# pop()            → remove top element
# top()            → get top element
# getMin()         → retrieve minimum element
#
# Example:
# s = MinStack()
# s.push(-2); s.push(0); s.push(-3)
# s.getMin()  → -3
# s.pop()
# s.top()     → 0
# s.getMin()  → -2
#
# Key question: how do you track the minimum as elements get popped?

class MinStack:
    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, val):
        self.stack.append(val)
        self.min_stack.append(val if not self.min_stack else min(val, self.min_stack[-1]))

    def pop(self):
        self.min_stack.pop()
        return self.stack.pop()

    def top(self):
        return self.stack[-1]

    def getMin(self):
        return self.min_stack[-1]
        




# Test
s = MinStack()
s.push(-2)
s.push(0)
s.push(-3)
print(s.getMin())  # -3
s.pop()
print(s.top())     # 0
print(s.getMin())  # -2
