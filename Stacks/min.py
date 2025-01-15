from Stack import Stack

class MinStack(Stack):
    def __init__(self):
        super().__init__()
        self.min_stack = Stack()
    
    def min(self):
        if self.min_stack.is_empty():
            return None
        return self.min_stack.peek()

    def push(self, item):
        if self.min() is None or item <= self.min():
            self.min_stack.push(item)
        super().push(item)

    def pop(self):
        item = super().pop()
        if item == self.min():
            self.min_stack.pop()
        return item
