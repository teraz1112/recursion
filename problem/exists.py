class BinaryTree:
    def __init__(self, data, left = None, right = None):
        self.data = data
        self.left = left
        self.right = right

def exists(root,key):
    # 関数を完成させてください
    if root is None:
        return False
    if root.data == key:
        return True
    if root.data > key:
        return exists(root.left,key)
    if root.data < key:
        return exists(root.right,key)
    return False

