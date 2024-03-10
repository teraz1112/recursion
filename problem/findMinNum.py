class SinglyLinkedListNode:
    def __init__(self, data):
        self.data = data
        self.next = None

def findMinNum(head):
    # 関数を完成させてください
    current = head
    min_num = current.data
    index=0
    min_index = index
    while current.next is not None:
        current = current.next
        index+=1
        if current.data <= min_num:
            min_num = current.data
            min_index = index
    return min_index
        
