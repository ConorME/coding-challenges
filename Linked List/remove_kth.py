from linked_list import Node

def remove_kth(head: Node, k: int) -> Node:
    if k == 0:
        return head.next
    current = head
    for _ in range(k - 1):
        if not current:
            return head  # If k is out of bounds, return the original list
        current = current.next
    if current.next:
        current.next = current.next.next 
    
    return head

