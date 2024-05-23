class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def zigzagLevelOrder(root):
    if not root:
        return []

    result = []
    queue = [root]
    level = 0

    while queue:
        level_size = len(queue)
        current_level = []

        for _ in range(level_size):
            node = queue.pop(0)
            current_level.append(node.val)

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        if level % 2 == 1:
            current_level.reverse()

        result.append(current_level)
        level += 1

    return result