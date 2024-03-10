class SinglyLinkedListNode:
    def __init__(self, data):
        self.data = data
        self.next = None

def deleteTail(head):
    # 関数を完成させてください
    if head is None:
        return None
    if head.next is None:
        return None
    current = head
    while current.next.next is not None:
        current = current.next
    current.next = None
    return head


