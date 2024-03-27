class BinaryTree:
    def __init__(self, data, left = None, right = None):
        self.data = data
        self.left = left
        self.right = right

def bstDelete(root,key):
    # 関数を完成させてください
        if not root:
            return
        if key < root.data:
            root.left = bstDelete(root.left, key)
        elif key > root.data:
            root.right = bstDelete(root.right, key)
        else:
            if not root.left and not root.right:
                root = None
            elif root.left and not root.right:
                root = root.left
            elif not root.right and root:
                root = root.right            
            else:
                root.data = getNext(root) # swap
                root.right = bstDelete(root.right, root.data) # delete the original node
        return root

# return left most of root.right
def getNext(root):
    root = root.right
    while root.left:
        root = root.left
    return root.data