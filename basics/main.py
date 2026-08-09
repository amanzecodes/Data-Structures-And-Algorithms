class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        
class LinkedList:
    def __init__(self, value):
        self.head=Node(value)
        self.tail=self.head
        self.length=1
    
    def printList(self):
        temp=self.head
        while temp is not None:
            print(temp.value)
            temp=temp.next
            
    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head=new_node
            self.tail=new_node
        temp=self.tail
        temp.next=new_node
        tail=temp
        self.length+=1
    
    def pop_node(self):
        if self.length == 0:
            return None
        if self.length == 1:
            self.head = None
            self.tail = None
            self.length -= 1
            return
        temp=self.head
        pre=self.head
        while temp.next:
            pre=temp
            temp=temp.next
        self.tail=pre
        self.tail.next=None
        self.length-=1
        return temp
    

my_linked_list = LinkedList(10)
my_linked_list.append(30)
my_linked_list.printList()
my_linked_list.pop_node()
my_linked_list.printList()