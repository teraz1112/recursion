class SinglyLinkedListNode:
    def __init__(self, data):
        self.data = data
        self.next = None

def linkedListLength(head):
    # 関数を完成させてください
    current=head
    length=0
    while current is not None:
        length+=1
        current=current.next
    return length

