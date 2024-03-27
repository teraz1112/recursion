class BinaryTree:
    def __init__(self, data, left = None, right = None):
        self.data = data
        self.left = left
        self.right = right

def preorderTraversalHelper(root, arr):
    if root is not None:
        arr.append(root.data)
        preorderTraversalHelper(root.left, arr)
        preorderTraversalHelper(root.right, arr)
    return arr

def preorderTraversal(root):
    arr=[]
    return preorderTraversalHelper(root, arr)
