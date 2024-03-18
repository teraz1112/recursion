class BinaryTree:
    def __init__(self, data, left = None, right = None):
        self.data = data
        self.left = left
        self.right = right

def bstSearch(root,key):
    # 関数を完成させてください

    iterator = root
    while iterator is not None:
        if iterator.data == key: return iterator
        if iterator.data > key:
            iterator = iterator.left
        else:
            iterator = iterator.right
    
    return None
