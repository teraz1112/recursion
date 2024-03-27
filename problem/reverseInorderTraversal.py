class BinaryTree:
    def __init__(self, data, left = None, right = None):
        self.data = data
        self.left = left
        self.right = right

def reverseInorderTraversal(root):
    # 関数を完成させてください
    arr = []
    return traversalHelper(root, arr)

def traversalHelper(root, arr):
    if root is not None:
        traversalHelper(root.right, arr)
        arr.append(root.data)
        traversalHelper(root.left, arr)

    return arr

