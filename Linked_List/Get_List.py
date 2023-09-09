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

####  ------- This is the GetList Block Code ------- ####

    def getList(self,index):
        if index < 0 or index >=self.length :
            return None
        temp=self.head
        for i in range(index):
            temp=temp.next
        return temp.value
####  ------- This is the GetList Block Code ------- ####

my_linked_list=Linked_list(1)
my_linked_list.appendList(2)
my_linked_list.appendList(3)
print("After Appending")
my_linked_list.print_list()
print("get list")
print(my_linked_list.getList(1))


