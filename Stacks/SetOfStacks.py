from typing import Optional
from Node import Node
from Stack import Stack

class SetOfStacks:
    def __init__(self, capacity: int):
        if capacity <= 0:
            raise ValueError("Capacity must be greater than zero.")
        self.capacity = capacity
        self.stacks = [Stack()]
        self.current_size = 0

    def push(self, item):
        if self.current_size == self.capacity:
            new_stack = Stack()
            self.stacks.insert(0, new_stack)
            self.current_size = 0
        self.stacks[0].push(item)
        self.current_size += 1

    def pop(self):
        if self.is_empty():
            raise Exception("Empty SetOfStacks: pop used on empty stacks.")
        item = self.stacks[0].pop()
        self.current_size -= 1
        if self.current_size == 0 and len(self.stacks) > 1:
            self.stacks.pop(0)
            self.current_size = self.capacity
        return item

    def peek(self):
        if self.is_empty():
            raise Exception("Empty SetOfStacks: peek used on empty stacks.")
        return self.stacks[0].peek()

    def is_empty(self):
        return len(self.stacks) == 1 and self.stacks[0].is_empty()

    def __repr__(self):
        return "\n".join([f"Stack {i}: {stack}" for i, stack in enumerate(self.stacks)])

