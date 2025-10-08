class Node:
    def __init__(self):
        self.data=None
        self.next=None
class LinkedList:
    def __init__(self):
        self.head=None
    def length(self):
        current=self.head
        if current==None:
            return
        count=1
        current=current.next
        while current!=self.head:
            current=current.next
            count+=1
        return count