class Node:
    def __init__(self, value):
        self.value=value
        self.next=None
        
class Solution:
    def has_loop(self):
        fast=self.head
        slow=fast.head
        
        while fast is not None and fast.next:
            fast = fast.next.next
            slow=slow.next
            
            if slow == fast:
                return True
        return False