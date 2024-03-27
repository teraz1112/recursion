class BinaryTree:
    def __init__(self, data, left = None, right = None):
        self.data = data
        self.left = left
        self.right = right


def levelOrderTraversal(root):
    # 関数を完成させてください
    if root is None:
        return []
    queue=[root]
    res=[]
    while set(queue) != {None}:
        node=queue.pop(0)
        if node is not None:
            res.append(node.data)
            queue.append(node.left)
            queue.append(node.right)
        else:
            res.append(None)
    return res