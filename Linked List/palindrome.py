from reverse import reverse

def palindrome(head):
    if not head or not head.next:
        return True  
    
    reversed_list = reverse(head)
    
    current = head
    current_reversed = reversed_list
    while current and current_reversed:
        if current.value != current_reversed.value:
            return False
        current = current.next
        current_reversed = current_reversed.next
    
    return True

