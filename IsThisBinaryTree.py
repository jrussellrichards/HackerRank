def inOrder(root):
    global flag, pre
    if root.left:
        inOrder(root.left)
    if pre < root.data:
        pre = root.data
    else:
        flag = False
        return
    if root.right:
        inOrder(root.right)


def check_binary_search_tree_(root):
    inOrder(root)
    global flag
    return flag

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


# https://www.hackerrank.com/challenges/is-binary-search-tree/problem?utm_campaign=challenge-recommendation&utm_medium=email&utm_source=24-hour-campaign


flag = True
pre = -1  # As all data are >= 0 so set pre = -1


check_binary_search_tree_(node3)