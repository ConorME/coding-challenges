from Stack import Stack

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

