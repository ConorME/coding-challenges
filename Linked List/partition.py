from linked_list import Node

def partition(head: Node, k: int):

    # couple of dummy nodes
    less_head = less_tail = Node(0)
    more_head = more_tail = Node(0)
    
    current = head
    while current:
        if current.value < k:
            less_tail.next = current
            less_tail = less_tail.next
        else:
            more_tail.next = current
            more_tail = more_tail.next
        current = current.next

    less_tail.next = more_head.next
    more_tail.next = None

    return less_head.next

