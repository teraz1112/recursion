class SinglyLinkedListNode:
    def __init__(self, data):
        self.data = data
        self.next = None

def insertAtPosition(head,position,data):
    # 関数を完成させてください
    current = head
    for i in range(position):
        if current.next is None:
            return head
        current = current.next
    new_node = SinglyLinkedListNode(data)
    new_node.next = current.next
    current.next = new_node
    return head