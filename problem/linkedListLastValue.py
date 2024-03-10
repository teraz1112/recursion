class SinglyLinkedListNode:
    def __init__(self, data):
        self.data = data
        self.next = None

def linkedListLastValue(head):
    # 関数を完成させてください
    current=head
    while current.next is not None:
        current=current.next
    return current.data

