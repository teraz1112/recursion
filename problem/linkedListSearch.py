class SinglyLinkedListNode:
    def __init__(self, data):
        self.data = data
        self.next = None

def linkedListSearch(head,data):
    current = head
    index = 0
    while current is not None:
        if current.data == data:
            return index
        current = current.next
        index += 1
    return -1
