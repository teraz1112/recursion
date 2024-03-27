
class BinaryTree:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def isMirror(left: BinaryTree, right: BinaryTree) -> bool:
    if left is None and right is None:
        return True
    if left is None or right is None:
        return False
    return (left.val == right.val) and isMirror(left.left, right.right) and isMirror(left.right, right.left)

def symmetricTree(root: BinaryTree) -> bool:
    if root is None:
        return True
    return isMirror(root.left, root.right)
