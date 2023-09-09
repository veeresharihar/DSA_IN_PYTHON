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

####  ------- This is the PrependList Block Code ------- ####

    def prependList(self,value):
        new_node=Node(value)
        if self.length == 0 :
            self.head=new_node
            self.tail=new_node
        else:
            new_node.next=self.head
            self.head=new_node
        self.length+=1

####  ------- This is the PrependList Block Code ------- ####
####  ------- This is the GetList Block Code ------- ####

    def getList(self,index):
        if index < 0 or index >=self.length :
            return None
        temp=self.head
        for i in range(index):
            temp=temp.next
        return temp
####  ------- This is the GetList Block Code ------- ####

####  ------- This is the InsertList Block Code ------- ####

    def InserList(self,index,value):
        if index<0 or index >self.length:
            return False
        if self.length==0:
            self.prependList(value)
        if self.length:
            self.appendList(value)
        new_node=Node(value)
        temp=self.getList(index-1)
        new_node.next=temp.next
        temp.next=new_node
        self.length+=1
        return True

####  ------- This is theInsertList Block Code ------- ####

my_linked_list=Linked_list(0)
my_linked_list.appendList(1)
my_linked_list.appendList(2)
my_linked_list.appendList(4)
my_linked_list.print_list()
print("after insertaion")
my_linked_list.InserList(3,3)
my_linked_list.print_list()

