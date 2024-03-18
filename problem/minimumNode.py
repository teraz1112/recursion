class BinaryTree:
    def __init__(self, data, left = None, right = None):
        self.data = data
        self.left = left
        self.right = right

def minimumNode(root):
    # 関数を完成させてください
    if root is None:
        return None
    if root.left is None:
        return root.data
    return minimumNode(root.left)

