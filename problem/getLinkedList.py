class SinglyLinkedListNode:
    def __init__(self, data):
        self.data = data
        self.next = None

class SinglyLinkedList:
    def __init__(self,data):
        self.head = data

def makeLinkedList(arr):
    # 関数を完成させてください
    for i in arr:
        if i == arr[0]:
            node=SinglyLinkedListNode(i)
            head=node
        else:
            node.next=SinglyLinkedListNode(i)
            node=node.next
    return head

def getLinkedList(arr):
    head=makeLinkedList(arr)
    current=head
    sentence=''
    while current is not None:
        sentence+=str(current.data)+'➡'
        current=current.next
        if current is None:
            sentence+='END'
    return sentence

print(getLinkedList([7,99,546]))
