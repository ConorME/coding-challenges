def kth_last(head: 'Node', k: int) -> 'Node':
    current = head
    length = 0

    while current:
        length += 1
        current = current.next

    current = head
    i = 0
    while i < length - k:
        current = current.next

    return current

