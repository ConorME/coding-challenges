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

def kth_last_2ptr(head: 'Node', k: int) -> 'Node':
    if not head or k <= 0:
        return None

    first = second = head

    for _ in range(k):
        if not first:
            return None #k is after the end of the array
        else:
            first = first.next


    while first:
        first = first.next
        second = second.next

    return second
