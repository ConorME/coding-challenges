from linked_list import Node

def reverse(head):

    prev = None
    current = head
    while current:
        temp = current.next
        current.next = prev
        prev = current
        current = temp

    return prev 
