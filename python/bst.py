class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class Bst:
    def __init__(self):
        self.root = None
    
    def add(self,  data): 
        newNode = Node(data)
        if self.root == None:
            self.root = newNode
        else:
            self.addNode(self.root, newNode)
    
    def addNode(self, currNode, newNode):
        if newNode.data < currNode.data:
            if currNode.left == None:
                currNode.left = newNode
            else:
                self.addNode(currNode.left, newNode)
        else:
            if currNode.right == None:
                currNode.right = newNode
            else:
                self.addNode(currNode.right, newNode)
        
            
    
    def preorder(self, curr):
        if curr == None:
            return
        print(curr.data)
        self.preorder(curr.left)
        self.preorder(curr.right)
    def inorder(self, curr):
        if curr != None:
            self.inorder(curr.left)
            print(curr.data)
            self.inorder(curr.right)
    def postorder(self, curr):
        if curr != None:
            self.postorder(curr.left)
            self.postorder(curr.right)
            print(curr.data)

b = Bst()
b.add(5)
b.add(4)
b.add(3)
b.add(2)
b.add(6)
b.add(7)
b.add(8)
b.preorder(b.root)
print('\n')
b.inorder(b.root)
                

        