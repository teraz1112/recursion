class SinglyLinkedListNode:
    def __init__(self, data):
        self.data = data
        self.next = None

def insertNodeInSorted(head,data):
    # 関数を完成させてください
    current = head
    new_node = SinglyLinkedListNode(data)
    if current is None:
        return new_node
    if current.data > data:
        new_node.next = current
        return new_node
    while current.next is not None:
        if current.next.data > data:
            new_node.next = current.next
            current.next = new_node
            return head
        current = current.next
    current.next = new_node
    return head