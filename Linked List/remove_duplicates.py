def remove_duplicates(head: 'Node') -> 'Node':
    """Removes duplicate nodes from a linked list while modifying the list in place."""
    if head is None:
        return None

    seen = set()
    current = head
    prev = None
    
    while current:
        if current.value in seen:
            prev.next = current.next
        else:
            seen.add(current.value)
            prev = current

        current = current.next

    return head
        
