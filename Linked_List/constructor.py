####  ------- This is the NewNode Creation Block Code ------- ####

class Node:
    def __init__(self,value):
        self.value=value
        self.next=None

####  ------- This is the NewNode Creation Block Code ------- ####

####  ------- This is the Constructor Block Code ------- ####

class Linked_list:
    def __init__(self,value):
        new_node=Node(value)
        self.head=new_node
        self.tail=new_node
        self.length=1

####  ------- This is the Constructor Block Code ------- ####

my_linked_list=Linked_list(4)
print(my_linked_list.head.value)

