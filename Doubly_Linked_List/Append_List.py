class Node:
    def __init__(self,value):
        self.value=value
        self.next=None
        self.prev=None
    

class Doubly_LL:
    def __init__(self,value):
        new_node=Node(value)
        self.head=new_node
        self.tail=new_node
        self.prev=new_node
        self.length = 1
        
####  ------- This is the PrintList Block Code ------- ####

    def print_list(self):
        temp=self.head
        while temp is not None:
            print(temp.value)
            temp=temp.next      

####  ------- This is the PrintList Block Code ------- ####
####  ------- This is the AppendList Block Code ------- ####

    def appendList(self,value):
        new_node=Node(value)
        if self.length == 0 :
            self.head=new_node
            self.tail=new_node
            self.prev=new_node
        else:
            self.tail.next=new_node
            new_node.prev=self.tail
            self.tail=new_node
        self.length+=1

####  ------- This is the AppendList Block Code ------- ####

my_linked_list=Doubly_LL(1)
print("After creating")
my_linked_list.print_list()
my_linked_list.appendList(2)
my_linked_list.appendList(3)
print("After Appending")
my_linked_list.print_list()
