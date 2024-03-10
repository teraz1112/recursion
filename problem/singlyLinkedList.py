class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self,data):
        self.head = data

node1=Node(7)
node2=Node(99)
node3=Node(546)

numList=LinkedList(node1)

numList.head.next=node2
numList.head.next.next=node3

current=numList.head

while current is not None:
    print(current.value)
    current=current.next