from linked_list import Node

def intersection(l1: Node, l2: Node):
    seen = set()
    
    # Add all nodes of l1 to the set
    current = l1
    while current:
        seen.add(current)
        current = current.next

    # Check if any node in l2 exists in l1
    current = l2
    while current:
        if current in seen:
            return current 
        current = current.next
        
    return None

