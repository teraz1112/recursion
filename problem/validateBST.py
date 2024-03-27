class BinaryTree:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

def validateBST(root):
    def isBSTUtil(node, min_val, max_val):
        if node is None:
            return True
        if node.data < min_val or node.data > max_val:
            return False
        return (isBSTUtil(node.left, min_val, node.data - 1) and
                isBSTUtil(node.right, node.data + 1, max_val))

    return isBSTUtil(root, float('-inf'), float('inf'))
    

