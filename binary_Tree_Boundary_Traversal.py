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
def TreeStructurePrint(root):
    if root is None:
        return
    print(root.data, end=" ")
    if root.left:
        print("Left:", root.left.data, end=" ")
    else:
        print("Left: None", end=" ")
    if root.right:
        print("Right:", root.right.data, end=" ")
    else:
        print("Right: None", end=" ")
    print()
    TreeStructurePrint(root.left)
    TreeStructurePrint(root.right)
    


def collectLeftBoundary(root, result):
    if root is None:
        return
    if root.left:
        result.append(root.data)
        collectLeftBoundary(root.left, result)
    elif root.right:
        result.append(root.data)
        collectLeftBoundary(root.right, result)
    return result

def collectRightBoundary(root, result):
    if root is None:
        return
    if root.right:
        collectRightBoundary(root.right, result)
        result.append(root.data)
    elif root.left:
        collectRightBoundary(root.left, result)
        result.append(root.data)


def collectLeaves(root, result):
    if root is None:
        return
    collectLeaves(root.left, result)
    if root.left is None and root.right is None:
        result.append(root.data)
    collectLeaves(root.right, result)


def findBoundaryTraversal(root):
    if root is None:
        return
    result = []
    result.append(root.data)
    collectLeftBoundary(root.left, result)
    collectLeaves(root.left, result)
    collectLeaves(root.right, result)
    collectRightBoundary(root.right, result)
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

print("Total Tree:",TreeStructurePrint(tree.root))  # Output: 5  Left: 3  Right: 7  Left: 2  Right: 4  Left: None  Right: None  Left: None  Right: None  Left: 6  Right: 8  Left: None  Right: None  Left: None  Right: None  Left: None  Right: None

print(findBoundaryTraversal(tree.root))  # Output: [5, 3, 2, 4, 6, 8]