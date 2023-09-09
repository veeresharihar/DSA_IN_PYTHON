class Node:
    def __init__(self,value):
        self.value=value
        self.next=None

class Linked_List:
    def __init__(self,value):
        new_node=Node(value)
        self.head=new_node
        self.tail=new_node
        self.length=1

    def printlist(self):
        temp=self.head
        while temp is not None:
            print(temp.value)
            temp=temp.next
    
    def append(self,value):
        new_node=Node(value)
        if self.length==0:
            self.head=new_node
            self.tail=new_node
        else:
            self.tail.next=new_node
            self.tail=new_node
        self.length+=1

    def prepend(self,value):
        new_node=Node(value)
        if self.length==0:
            self.head=new_node
            self.tail=new_node
        else:
            new_node.next=self.head
            self.head=new_node
        self.length+=1

    def get(self,index):
        temp=self.head
        for _ in range(index):
            temp=temp.next
        return temp


    def insert(self,index,value):
        if index < 0 or index > self.length:
            return False
        if index==0:
            return self.prepend(value)
        if index==self.length:
            return self.append(value)
        new_node=Node(value)
        temp=self.get(index-1)
        new_node.next=temp.next
        temp.next=new_node
        self.length+=1
        return True
    
    

mylinkedlist=Linked_List(1) 
mylinkedlist.printlist()
print("After Appending")   
mylinkedlist.append(2)
mylinkedlist.append(3)
mylinkedlist.append(4)
mylinkedlist.printlist()
print("After Prepending")
mylinkedlist.prepend(0)
mylinkedlist.printlist()
print("Get Method")
print(mylinkedlist.get(2))
print("After Inserting")
mylinkedlist.insert(2,6)
mylinkedlist.insert(3,7)
mylinkedlist.printlist()


