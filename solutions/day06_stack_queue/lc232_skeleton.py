# LC 232 - Implement Queue using Stacks
#
# Implement a FIFO queue using only two stacks.
#
# MyQueue()    → initialize
# push(x)     → push to back of queue
# pop()       → remove from front, return it
# peek()      → get front element
# empty()     → return True if empty
#
# Example:
# q = MyQueue()
# q.push(1); q.push(2)
# q.peek()   → 1
# q.pop()    → 1
# q.empty()  → False
#
# Key question: stacks are LIFO, queue is FIFO.
# How do you reverse the order using two stacks?

class MyQueue:
    def __init__(self):
        self.stack_in = []
        self.stack_out = []

    def _transfer(self):
        if not self.stack_out: # only transfer when out is empty
            while self.stack_in:
                self.stack_out.append(self.stack_in.pop())

    def push(self, val):
        self.stack_in.append(val)

    def pop(self):
        self._transfer()
        return self.stack_out.pop()

    def peek(self):
        self._transfer()
        return self.stack_out[-1]

    def empty(self):
        return not self.stack_in and not self.stack_out


# Test
q = MyQueue()
q.push(1)
q.push(2)
print(q.peek())   # 1
print(q.pop())    # 1
print(q.empty())  # False
