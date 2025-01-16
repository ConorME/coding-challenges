from Stack import Stack

def sort_stack(stack: Stack):
    if stack.is_empty():
        return
    pivot = stack.pop()
    higher = Stack()
    lower = Stack()

    while not stack.is_empty():
        if stack.peek() >= pivot:
            higher.push(stack.pop())
        else:
            lower.push(stack.pop())

    sort_stack(higher)
    sort_stack(lower)

    while not higher.is_empty():
        stack.push(higher.pop())

    stack.push(pivot)

    while not lower.is_empty():
        stack.push(lower.pop())

    return stack

class StackSort:
    def __init__(self):
        self.stack = Stack()

    def push(self, item):
        if self.stack.is_empty() or self.stack.peek() >= item:
            self.stack.push(item)
        else:
            temp = Stack()
            while not self.stack.is_empty() and self.stack.peek() < item:
                temp.push(self.stack.pop())

            # Push our value onto its correct location in the Stack
            self.stack.push(item)

            while not temp.is_empty():
                self.stack.push(temp.pop())

    def pop(self):
        return self.stack.pop()

    def peek(self):
        return self.stack.peek()

    def is_empty(self):
        return self.stack.is_empty()

    def __repr__(self):
        return f"StackSort(stack={repr(self.stack)})"


