class SinglyLinkedListNode:
    def __init__(self, data):
        self.data = data
        self.next = None

def reproduceByN(head,n):
    newList = SinglyLinkedListNode(None)
    newHead = newList
    
    while n > 0:
        iterator = head
        while iterator != None:
            newList.next = SinglyLinkedListNode(iterator.data)
            newList = newList.next
            iterator = iterator.next
        n -= 1
    return newHead.next
                
