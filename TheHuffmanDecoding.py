# Enter your code here. Read input from STDIN. Print output to STDOUT
import string


# Version para hackerank
# def decodeHuff(root, s):
#     #Enter Your Code Here
#     aux = root
#     word = ""
#     abc = string.printable
#     for i in range(len(s)):
#         if(s[i] == "0"):
#             if aux:
#                 aux = aux.left
#                 if aux:
#                     if(aux.data in abc):
#                         word += aux.data
#                         aux = root
#         else:
#             if aux:
#                 aux = aux.right
#                 if aux:
#                     if aux.data in abc:
#                         word += aux.data
#                         aux = root
#     print(word)
                

def decodeHuff(root, s):
    #Enter Your Code Here
    aux = root
    word = ""
    abc = string.printable
    for i in range(len(s)):
        if aux:
            if(s[i] == "0"):
                    aux = aux.left
                    if aux:
                        if(aux.data in abc):
                            word += aux.data
                            aux = root
            else:
                    aux = aux.right
                    if aux:
                        if aux.data in abc:
                            word += aux.data
                            aux = root
    print(word)
                
        


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

    node1 = Node(None)
    node2 = Node(None)
    node3 = Node('A')
    node4 = Node('B')
    node5 = Node('C')
    node1.left = node2
    node1.right = node3
    node2.left = node4
    node2.right = node5


s='1001011'

decodeHuff(node1,s)