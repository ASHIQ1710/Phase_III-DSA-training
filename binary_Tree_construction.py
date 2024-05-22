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
    

# Example usage:
tree = Tree()
tree.insert(5)
tree.insert(3)
tree.insert(7)
tree.insert(2)
tree.insert(4)
tree.insert(6)
tree.insert(8)

print("Inorder traversal:")
tree.print_inorder()

print("\nPreorder traversal:")
tree.print_preorder()

print("\nPostorder traversal:")
tree.print_postorder()

print("\nLevel order traversal:")# [[5], [3, 7], [2, 4, 6, 8]]
