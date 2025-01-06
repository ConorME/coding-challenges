class Node:
    """Basic linked list node."""
    def __init__(self, value):
        self.value = value
        self.next = None

def generate_linked_list(size):
    """Generates a random linked list for testing."""
    import random
    head = Node(random.randint(0, 100))
    current = head
    for _ in range(size - 1):
        current.next = Node(random.randint(0, 100))
        current = current.next
    return head

