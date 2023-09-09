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

####  ------- This is the AppendList Block Code ------- ####

    def appendList(self,value):
        new_node=Node(value)
        if self.length == 0 :
            self.head=new_node
            self.tail=new_node
        else:
            self.tail.next=new_node
            self.tail=new_node
        self.length+=1

####  ------- This is the AppendList Block Code ------- ####


####  ------- This is the PopList Block Code ------- ####

    def popList(self):
        if self.length==0:
            return None
        temp=self.head
        pre=self.head
        while (temp.next):
            pre=temp
            temp=temp.next
        self.tail=pre
        self.tail.next=None
        self.length-=1
        if self.length==0:
            self.head=None
            self.tail=None
        return temp
    
####  ------- This is the PopList Block Code ------- ####

my_linked_list=Linked_list(1)
my_linked_list.appendList(2)
my_linked_list.appendList(3)
my_linked_list.appendList(4)
print("After Appending")
my_linked_list.print_list()
my_linked_list.popList()
print("After poping")
my_linked_list.print_list()
