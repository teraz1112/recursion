class BinaryTree:
    def __init__(self, data, left = None, right = None):
        self.data = data
        self.left = left
        self.right = right

def inorderTraversal(root):
    # 関数を完成させてください
    arr = []
    return traversalHelper(root, arr)

def traversalHelper(root, arr):
    if root is not None:
        traversalHelper(root.left, arr)
        arr.append(root.data)
        traversalHelper(root.right, arr)
    return arr

