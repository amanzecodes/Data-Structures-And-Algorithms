class Node:
    def __init__(self,value):
        self.value=value
        self.next=None
        
class Solution:
    def find_middle_node(self):
        slow = self.head
        fast = self.head
        
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
        
        return slow