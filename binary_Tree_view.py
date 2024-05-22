class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class Tree:
    def __init__(self):
        self.root = None

    def insert(self, data):
        if self.root is None:
            self.root = Node(data)
        else:
            self._insert_recursive(data, self.root)

    def _insert_recursive(self, data, node):
        if data < node.data:
            if node.left is None:
                node.left = Node(data)
            else:
                self._insert_recursive(data, node.left)
        else:
            if node.right is None:
                node.right = Node(data)
            else:
                self._insert_recursive(data, node.right)

    def print_inorder(self):
        self._print_inorder_recursive(self.root)

    def _print_inorder_recursive(self, node):
        if node:
            self._print_inorder_recursive(node.left)
            print(node.data, end=" ")
            self._print_inorder_recursive(node.right)

    def print_preorder(self):
        self._print_preorder_recursive(self.root)

    def _print_preorder_recursive(self, node):
        if node:
            print(node.data, end=" ")
            self._print_preorder_recursive(node.left)
            self._print_preorder_recursive(node.right)

    def print_postorder(self):
        self._print_postorder_recursive(self.root)

    def _print_postorder_recursive(self, node):
        if node:
            self._print_postorder_recursive(node.left)
            self._print_postorder_recursive(node.right)
            print(node.data, end=" ")

# Level order traversal
def levelOrderTraversal(root):
    if root is None:
        return
    result=[]
    Q=[root]
    while len(Q)>0:
        n=len(Q)
        subresult=[]
        for i in range(n):
            # remove the first element from the list
            node=Q.pop(0)
            # add the value of the node to the subresult
            subresult.append(node.data)
            # add the left child to the queue
            if node.left is not None:
                Q.append(node.left)
            # add the right child to the queue
            if node.right is not None:
                Q.append(node.right)
        result.append(subresult)
    return result

def findLeftView(root):
    if root is None:
        return
    result=[]
    Q=[root]
    while len(Q)>0:
        n=len(Q)
        for i in range(n):
            node=Q.pop(0)
            if i==0:
                result.append(node.data)
            if node.left is not None:
                Q.append(node.left)
            if node.right is not None:
                Q.append(node.right)
    return result

def findRightView(root):
    if root is None:
        return
    result=[]
    Q=[root]
    while len(Q)>0:
        n=len(Q)
        for i in range(n):
            node=Q.pop(0)
            if i==n-1:
                result.append(node.data)
            if node.left is not None:
                Q.append(node.left)
            if node.right is not None:
                Q.append(node.right)
    return result

def findTopView(root):
    if root is None:
        return
    result=[]
    Q=[(root,0)]
    d={}
    while len(Q)>0:
        node,hd=Q.pop(0)
        if hd not in d:
            d[hd]=node.data
        if node.left is not None:
            Q.append((node.left,hd-1))
        if node.right is not None:
            Q.append((node.right,hd+1))
    for i in sorted(d.keys()):
        result.append(d[i])
    return result

def findBottomView(root):
    if root is None:
        return
    result=[]
    Q=[(root,0)]
    d={}
    while len(Q)>0:
        node,hd=Q.pop(0)
        d[hd]=node.data
        if node.left is not None:
            Q.append((node.left,hd-1))
        if node.right is not None:
            Q.append((node.right,hd+1))
    for i in sorted(d.keys()):
        result.append(d[i])
    return result

# Example usage:
tree = Tree()
tree.insert(5)
tree.insert(3)
tree.insert(7)
tree.insert(2)
tree.insert(4)
tree.insert(6)
tree.insert(8)

print("level order traversal:",levelOrderTraversal(tree.root)) # [[5], [3, 7], [2, 4, 6, 8]]
print("left view:",findLeftView(tree.root)) # [5, 3, 2]
print("right view:",findRightView(tree.root)) # [5, 7, 8]
print("top view:",findTopView(tree.root)) # [2, 3, 5, 7, 8]
print("bottom view:",findBottomView(tree.root)) # [2, 3, 6, 7, 8]
