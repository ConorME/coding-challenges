import Stack from Stack

def MyQueue:
    def __init__(self):
        self.s1 = Stack()
        self.s2 = Stack()

    def _transfer(self):
        while first:
            self.s2.push(self.s1.pop())

    def add(self, item):
        self.s1.push(item)

    def remove(self):
        if (self.s2.isEmpty):
            _transfer(self)
        self.s2.pop()

    def peek(self):
        if(self.s2.isEmpty):
            _transfer(self)
        self.s2.peek()

