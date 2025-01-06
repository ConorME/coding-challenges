from linked_list import Node
from remove_kth import remove_kth

def remove_middle(head):
    count = 0
    current = head

    while current:
        current = current.next
        count += 1

    return remove_kth(head, count)



