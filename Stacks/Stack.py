from typing import Optional
from Node import Node

class EmptyStackError(Exception):
    """Exception raised when performing operations on an empty stack."""
    pass

class Stack:
    def __init__(self):
        self.top: Optional[Node] = None
        
    def push(self, item):
        new_node = Node(item)
        new_node.next = self.top
        self.top = new_node
        
    def pop(self):
        if self.top is None:
            raise EmptyStackError("pop used on empty stack") 
        item = self.top.data
        self.top = self.top.next
        return item
        
    def peek(self):
        if self.top is None:
            raise EmptyStackError("peek used on empty stack")
        return self.top.data
        
    def is_empty(self):
        return self.top is None
    
    def __repr__(self) -> str:
        elements = []
        current = self.top
        while current:
            elements.append(repr(current.data))
            current = current.next
        return "Stack(" + " -> ".join(elements) + ")"

