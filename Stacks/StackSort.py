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

class StackSort(Stack):
    def __init__(self):
        super().__init__()

    def push(self, item):
        if super().is_empty() or super().peek() >= item:
            super().push(item)
        else:
            temp = Stack()
            while not super().is_empty() and super().peek() < item:
                temp.push(super().pop())

            # Push our value onto its correct location in the Stack
            super().push(item)

            while not temp.is_empty():
                super().push(temp.pop())

