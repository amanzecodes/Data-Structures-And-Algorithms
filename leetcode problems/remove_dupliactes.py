#Pattern Recognised: 'Anchor + Runner'

#' One pointer current chooses an element. Another pointer(runner) scnas ahead looking for elements that conflict with it'


class Node:
    def __init__(self, value):
        self.value=value
        self.next=None
        
class Solution:
    def __init__(self, value):
        self.head=Node(value)
        self.tail=self.head
        self.length=1
    
    def remove_duplicates(self):
        current=self.head
        runner=self.head
        
        while current is not None:
            runner=current
            while runner.next:
                if runner.next.value == current.value:
                    runner.next=runner.next.next
                else:
                    runner=runner.next
            current=current.next