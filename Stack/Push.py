class Node:
    def __init__(self, value):
        self.value=value
        self.next=None
    
class Stack:
    def __init__(self,value):
        new_node=Node(value)
        self.top=new_node
        self.bottom=new_node
        self.height=1
    
    def print_stack(self):
        temp=self.top
        while temp is not None:
            print(temp.value)
            temp=temp.next

    def push(self,value):
        new_node=Node(value)
        if self.height==0:
            self.top=new_node
        new_node.next=self.top
        self.top=new_node
        self.height+=1
        
mystack=Stack(1)
mystack.print_stack()
print("After Pushing")
mystack.push(2)
mystack.push(3)
mystack.push(4)
mystack.print_stack()