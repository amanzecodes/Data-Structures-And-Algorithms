#Pattern:Fast and Slow pointers
class Node:
    def __init__(self,value):
        self.value=value
        self.next=None
        
class Solution:
    
    def __init__(self, value):
        self.head=Node(value)
        self.tail=self.head
        self.length=1
        
    def find_middle_node(self):
        slow = self.head
        fast = self.head
        
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
        
        return slow
    
    def append(self, value):
            new_node = Node(value)
            if self.head is None:
                self.head=new_node
                self.tail=new_node
            self.tail.next=new_node
            self.tail=new_node
            self.length+=1


my_linked_list = Solution(1)
my_linked_list.append(2)
my_linked_list.append(3)
my_linked_list.append(4)
my_linked_list.append(5)

print( my_linked_list.find_middle_node().value )