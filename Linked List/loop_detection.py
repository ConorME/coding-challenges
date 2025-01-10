from linked_list import Node

# Tortoise and Hare
def loop_detection(head: Node) -> bool:
    fast = slow = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

        if slow == fast:
            return True

    return false


