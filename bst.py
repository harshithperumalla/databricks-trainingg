class BST:
    def __init__(self, key):
        self.key = key
        self.lnode = None
        self.rnode = None
    
    def insert(self, data):
        if data < self.key:
            if self.lnode is None:
                self.lnode = BST(data)
            else:
                self.lnode.insert(data)
        elif data > self.key:
            if self.rnode is None:
                self.rnode = BST(data)
            else:
                self.rnode.insert(data)

    def search(self, data):
        if self.key == data:
            print(f"Node {data} is present in the tree")
            return True
        if data < self.key:
            if self.lnode:
                return self.lnode.search(data)
            else:
                print(f"Node {data} is NOT present in the tree")
                return False
        else:
            if self.rnode:
                return self.rnode.search(data)
            else:
                print(f"Node {data} is NOT present in the tree")
                return False

    def inorder(self):
        if self.lnode:
            self.lnode.inorder()
        print(self.key, end=" ")
        if self.rnode:
            self.rnode.inorder()
            
    def preorder(self):
        print(self.key, end=" ")
        if self.lnode:
            self.lnode.preorder()
        if self.rnode:
            self.rnode.preorder()

    def postorder(self):
        if self.lnode:
            self.lnode.postorder()
        if self.rnode:
            self.rnode.postorder()
        print(self.key, end=" ")  
        
    def delete(self,data):
      if self.key is None:
          print("node is not there in")
          return
      if self.key<data:
          if self.lnode:
              self.lnode=self.lnode.delete(data)
          else:
              print("node is not in given")
      elif self.key>data:
          if self.rnode:
             self.rnode=self.rnode.delete(data)
          else:
              print("it is not node were")
        

root = BST(8)
print("Root:", root.key)

list_values = [1, 4, 35, 64, 3, 2, 5, 12]
for i in list_values:
    root.insert(i)

print("\nInorder Traversal:", end=" ")
root.inorder()
print()

root.search(10)
root.search(7)
root.search(5)

print("\nPreorder Traversal:", end=" ")
root.preorder()
print()

print("\nInorder Traversal:", end=" ")
root.inorder()
print()

print("\nPostorder Traversal:", end=" ")
root.postorder()
print()
