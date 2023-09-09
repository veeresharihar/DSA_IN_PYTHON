class Node:
    def __init__(self,value):
        self.value=value
        self.next=None

class Linked_list:
    def __init__(self,value):
        new_node=Node(value)
        self.head=new_node
        self.tail=new_node
        self.length=1

####  ------- This is the PrintList Block Code ------- ####

    def print_list(self):
        temp=self.head
        while temp is not None:
            print(temp.value)
            temp=temp.next      

####  ------- This is the PrintList Block Code ------- ####

my_linked_list=Linked_list(4)
my_linked_list.print_list()





