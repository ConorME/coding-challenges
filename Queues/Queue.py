 from typing import Optional

class Node:
    def __init__(self, data):
        self.data = data
        self.next: Optional['Node'] = None

class EmptyQueueError(Exception):
    """Raised when performing operations on an empty queue."""
    pass

class Queue:
    def __init__(self):
        self.front: Optional[Node] = None
        self.rear: Optional[Node] = None
        
    def enqueue(self, item):
        new_node = Node(item)
        if self.rear is None:
            self.front = self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node
        
    def dequeue(self):
        if self.front is None:
            raise EmptyQueueError("dequeue used on empty queue")
        item = self.front.data
        self.front = self.front.next
        if self.front is None:
            self.rear = None  # Reset rear if the queue becomes empty
        return item
        
    def peek(self):
        if self.front is None:
            raise EmptyQueueError("peek used on empty queue")
        return self.front.data
        
    def is_empty(self):
        return self.front is None

    def __repr__(self) -> str:
        elements = []
        current = self.front
        while current:
            elements.append(repr(current.data))
            current = current.next
        return "Queue(" + " -> ".join(elements) + ")"
      
