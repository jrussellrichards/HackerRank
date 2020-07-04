class Node:
    def __init__(self, info): 
        self.info = info  
        self.left = None  
        self.right = None 
        self.level = None 

    def __str__(self):
        return str(self.info) 

class BinarySearchTree:
    def __init__(self): 
        self.root = None

    def create(self, val):  
        if self.root == None:
            self.root = Node(val)
        else:
            current = self.root
         
            while True:
                if val < current.info:
                    if current.left:
                        current = current.left
                    else:
                        current.left = Node(val)
                        break
                elif val > current.info:
                    if current.right:
                        current = current.right
                    else:
                        current.right = Node(val)
                        break
                else:
                    break


tree = BinarySearchTree()
t = int(input())

arr = list(map(int, input().split()))

for i in range(t):
    tree.create(arr[i])

def postOrder(root):
    if root:
        postOrder(root.left)
        postOrder(root.right)
        print(root.info, end=' ')


def preOrder(root):
    if(root):
        print(root.info, end=' ')
        preOrder(root.left)
        preOrder(root.right)

def inOrder(root):
    if(root):
        inOrder(root.left)
        print(root.info, end=' ')
        inOrder(root.right)

print('postOrder',postOrder(tree.root))
print('inOrder',inOrder(tree.root))
print('preOrder',preOrder(tree.root))

# 6
# 1 2 5 3 6 4