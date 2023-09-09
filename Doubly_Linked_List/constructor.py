class Node:
    def __init__(self,value):
        self.value=value
        self.next=None
        self.prev=None
        self.length = 1
    

class Doubly_LL:
    def __init__(self,value):
        new_node=Node(value)
        self.head=new_node
        self.tail=new_node
        self.prev=new_node
        
my_linked_list=Doubly_LL(4)
print(my_linked_list.head.value)