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
####  ------- This is the Poping First Item from List Block Code ------- ####

    def popfirstList(self):
        if self.length == 0 :
            return None
        temp=self.head
        self.head=self.head.next
        temp.next=None
        self.length+=1
        if self.length==0:
            self.tail=None
        return temp.value

####  ------- This is the Poping First Item from List Block Code ------- ####




####  ------- This is the InsertList Block Code ------- ####

    def removeList(self,index):
        if index<0 or index >=self.length:
            return None
        if self.length==0:
            self.popfirstList()
        if self.length:
            self.popList()
        prev=self.getList(index-1)
        temp=prev.next
        prev.next=temp.next
        temp.next=None
        self.length-=1
        return temp.value

####  ------- This is theInsertList Block Code ------- ####

my_linked_list=Linked_list(0)
my_linked_list.appendList(1)
my_linked_list.appendList(2)
my_linked_list.appendList(3)

my_linked_list.removeList(2)

my_linked_list.print_list()


