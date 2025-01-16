from Stack import Stack

def sort_stack(stack: Stack):
    if stack.is_empty():
        return
    pivot = stack.pop()
    higher = Stack()
    lower = Stack()

    while stack:
        if stack.peek() >= pivot:
            higher.push(stack.pop())
        else:
            lower.push(stack.pop())

    sort_stack(higher)
    sort_stack(lower)

    while higher:
        stack.push(higher.pop())

    stack.push(pivot)

    while lower:
        stack.push(lower.pop())

    return stack

class StackSort(Stack):
    def __init__(self):
        super().__init__()

    def push(item):
        if self.is_empty() or self.peek() >= item:
            self.push(item)
        else:
            temp = Stack()
            while self.peek() < item:
                temp.push(self.pop())

            # Push our value onto its correct location in the Stack
            self.push(item)

            while temp:
                self.push(temp.pop())

