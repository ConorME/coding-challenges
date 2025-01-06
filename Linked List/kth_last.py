from linked_list import Node

def kth_last_two_pointer(head: Node, k: int) -> Node:
    first = second = head
    for _ in range(k):
        if not first:
            return None
        first = first.next
    while first:
        first, second = first.next, second.next
    return second

def kth_last_length(head: Node, k: int) -> Node:
    length = 0
    current = head
    while current:
        length += 1
        current = current.next
    if k > length:
        return None
    current = head
    for _ in range(length - k):
        current = current.next
    return current

