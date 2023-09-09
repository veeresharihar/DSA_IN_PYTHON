class Node:
    def __init__(self, value):
        self.value=value
        self.next=None
    
class Queue:
    def __init__(self,value):
        new_node=Node(value)
        self.first=new_node
        self.last=new_node
        self.length=1
    
    def print_queue(self):
        temp=self.first
        while temp is not None:
            print(temp.value)
            temp=temp.next

    def enqueue(self,value):
        new_node=Node(value)
        if self.length==0:
            self.first=new_node
            self.last=new_node
        self.last.next=new_node
        self.last=new_node
        self.length+=1



mystack=Queue(1)
mystack.print_queue()
mystack.enqueue(2)
mystack.enqueue(3)
mystack.enqueue(4)
print("After Adding to Queue")
mystack.print_queue()