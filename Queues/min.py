from Stack import Stack, Node

class MinStack(Stack):
    def __init__(self):
        super().__init__()
        self.min_stack = Stack()  

    def push(self, item):
        super().push(item)
        if self.min_stack.is_empty() or item <= self.min_stack.peek():
            self.min_stack.push(item)

    def pop(self):
        if self.is_empty():
            raise Exception("Empty Stack Exception: pop used on empty stack")
        item = super().pop()
        if item == self.min_stack.peek():
            self.min_stack.pop()
        return item

    def get_min(self):
        if self.min_stack.is_empty():
            raise Exception("Stack is empty, no minimum value.")
        return self.min_stack.peek()

