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
        self.tail.next=new_node
        self.tail=new_node
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
    
    def prepend(self, value):
        new_node=Node(value)
        if self.length == 0:
            self.head=new_node
            self.tail=new_node
        new_node.next=self.head
        self.head=new_node
        self.length+=1
        return True
    
    def pop_first(self):
        temp=self.head
        if temp is None:
            return None
        if self.length == 1:
            self.head = None
            self.tail = None
        self.head=temp.next
        temp.next=None
        return temp.value
    
    def get(self, index):
        if index < 0 or index >= self.length:
            return None
        temp=self.head
        for _ in range(index):
            temp=temp.next
        return temp
    
    def set_value(self, index, value):
        temp=self.get(index)
        if temp:
            temp.value=value
            return True
        return False
        
my_linked_list = LinkedList(0)
my_linked_list.append(1)
my_linked_list.append(2)
my_linked_list.append(3)

print(my_linked_list.get(2))