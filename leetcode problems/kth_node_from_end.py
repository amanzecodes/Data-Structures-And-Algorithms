#Pattern: Two Pointers with a fixed gap
class Node:
    def __init__(self, value):
        self.value=value
        self.next=None
        

def kth_node_from_end(ll, k):
    fast=ll.head
    slow=ll.head
    
    for _ in range(k):
        if fast is None:
            return None
        fast=fast.next
    
    while fast is not None:
        slow=slow.next
        fast=fast.next
        
    return slow