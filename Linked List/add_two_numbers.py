from linked_list import Node

def addTwoNumbers(self, l1: Node, l2: Node):
        root = Node()
        tail = root
        value = 0
        carry = 0
        
        while(l1 != None or l2 != None or carry != 0):
            
            # Add the values together if they exist.
            if(l1 != None):
                value += l1.val
            if(l2 != None):
                value += l2.val
            
            # Add the carry and exhaust it.
            value += carry
            carry = 0
            
            # Carry the one if our value is greater than 10.
            # And set the value to the remainder.
            if value >= 10:
                carry = 1
                value = value % 10
            
            if(l1 != None):
                l1 = l1.next
            if(l2 != None):
                l2 = l2.next
            
            tail.next = Node(value)
            tail = tail.next
            value = 0
        
        return root.next
            
