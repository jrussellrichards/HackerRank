

def check_binary_search_tree(root):
    
    def checkFalse(root):
        if root:
            
            if(root.left):
                
                if(root.data <= root.left.data):
                    return False
                
            if(root.right):
                if(root.data >=root.right.data):
                    
                    return False
            if(checkFalse(root.left) == False):
                return False
            elif(checkFalse(root.right) == False):
                return False
    
    if(checkFalse(root) == False):
        return False
    else:
        return True
    

def check_binary_search_tree_(root):
    l = []
    traverse(root,l)
    if(False in l):
        return False
    else:
        return True
def traverse(node,l):
    if(node):
        if(node.left):
            if(node.left.data >= node.data):
                l.append(False)
                return
            
        if(node.right):
            if(node.right.data <= node.data):
                l.append(False)
                return
        traverse(node.left,l)
        traverse(node.right,l)

    #     4
    #    2  5
    #   1  3   6
    #         8


def PreOrder(root):
    if root:
        print(root.data)
        PreOrder(root.left)
        PreOrder(root.right)


class Node:
    data = None
    left = None
    right = None

    def __init__(self, data):
        self.data = data

    def insert(self, d):
        if self.data == d:
            return False
        elif d < self.data:
            if self.left:
                return self.left.insert(d)
            else:
                self.left = Node(d)
                return True
        else:
            if self.right:
                return self.right.insert(d)
            else:
                self.right = Node(d)
        return True


if __name__ == "__main__":

    node3 = Node(3)
    node5 = Node(5)
    node2 = Node(2)
    node1 = Node(1)
    node4 = Node(4)
    node6 = Node(6)
    node3.left = node5
    node3.right = node2
    node2.left = node6
    node5.right = node4
    node5.left = node1


  

    print(check_binary_search_tree(node3))
