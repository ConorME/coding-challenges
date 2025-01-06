from linked_list import Node

def remove_duplicates_set(head: Node) -> Node:
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

def remove_duplicates_no_buffer(head: Node) -> Node:
    current = head
    while current:
        runner = current
        while runner.next:
            if runner.next.value == current.value:
                runner.next = runner.next.next
            else:
                runner = runner.next
        current = current.next
    return head

