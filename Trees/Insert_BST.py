class Node:
    def __init__(self, value):
        self.value = value
        self.left=None
        self.right=None

class BST:
    def __init__(self):
        self.root=None

    def insert(self,value):
        new_node=Node(value)
        if self.root==None:
            self.root=new_node
        temp=self.root
        while True:
            if temp.value==new_node.value:
                return False
            if temp.value < new_node.value:
                if temp.left==None:
                    temp.left=new_node
                    return True
                temp=temp.left
            else:
                if temp.right==None:
                    temp.right=new_node
                    return True
                temp=temp.right

mybinarysearchtree=BST()
#print(mybinarysearchtree)
mybinarysearchtree.insert(2)
mybinarysearchtree.insert(1)
mybinarysearchtree.insert(3)
print(mybinarysearchtree.root.value)
print(mybinarysearchtree.root.left.value)
print(mybinarysearchtree.root.right.value)