class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def maximumDepth(root):
    if root is None:
        return -1
    else:
        left_depth = maximumDepth(root.left)
        right_depth = maximumDepth(root.right)
        return max(left_depth, right_depth) + 1
