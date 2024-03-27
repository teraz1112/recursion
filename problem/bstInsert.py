class BinaryTree:
    def __init__(self, data, left = None, right = None):
        self.data = data
        self.left = left
        self.right = right

def bstInsert(root,key):
    # 関数を完成させてください
    temp = root

    while temp is not None:
        if key == temp.data:
            return root
        elif key < temp.data:
            if temp.left is None:
                temp.left = BinaryTree(key)
                return root
            else:
                temp = temp.left
        else:
            if temp.right is None:
                temp.right = BinaryTree(key)
                return root
            else:
                temp = temp.right