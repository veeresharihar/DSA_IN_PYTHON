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

    def prependList(self,value):
            new_node=Node(value)
            if self.length == 0 :
                self.head=new_node
                self.tail=new_node
                self.prev=new_node
            self.head.prev=new_node
            new_node.next=self.head
            self.head=new_node
            self.length+=1

    def getList(self,index):
        if index<0 or index>self.length:
            return None
        temp=self.head
        for i in range(index):
            temp=temp.next
        return temp


    def insertlist(self,index,value):
        if index<0 or index>self.length:
            return None
        if index==0:
            return self.prependList(value)
        if index==self.length:
            return self.appendList(value)
        new_node=Node(value)
        temp=self.getList(index)
        temp1=self.getList(index-1)
        new_node.next=temp
        temp.prev=new_node
        temp1.next=new_node
        new_node.prev=temp1

my_linked_list=Doubly_LL(1)
print("After creating")
my_linked_list.print_list()
my_linked_list.appendList(2)
my_linked_list.appendList(3)
print("After Appending")
my_linked_list.print_list()
print("After Prepending")
my_linked_list.prependList(4)
my_linked_list.print_list()
print("After Inserting")
my_linked_list.insertlist(2,5)
my_linked_list.print_list()
