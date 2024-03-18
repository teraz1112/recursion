import math

class BinaryTree:
    def __init__(self, data, left = None, right = None):
        self.data = data
        self.left = left
        self.right = right

def sortedArrToBST(numberList):
    # 関数を完成させてください
    
    if len(numberList) == 0: return None
    return sortedArrToBSTHelper(numberList, 0, len(numberList) - 1)


def sortedArrToBSTHelper(arr, start, end):
    if start == end: return BinaryTree(arr[start], None, None)

    mid = math.floor((start + end) / 2)

    left = None
    if mid - 1 >= start:
        left = sortedArrToBSTHelper(arr, start, mid - 1)
    
    right = None
    if mid + 1 <= end:
        right = sortedArrToBSTHelper(arr, mid + 1, end)
    
    root = BinaryTree(arr[mid], left, right)
    return root
