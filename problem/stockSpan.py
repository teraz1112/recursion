class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.head = None
    
    def push(self,data):
        tmp = self.head
        self.head = Node(data)
        self.head.next = tmp
    
    def pop(self):
        if self.head is None :
            return 
        tmp = self.head
        self.head = self.head.next 
        return tmp.data
    
    def peek(self):
        if self.head is None:
            return
        return self.head.data


def stockSpan(stocks):
    # ここから書きましょう
    result = []
    stack = Stack()

    for i in range(len(stocks)):
        count = 1
        while(stack.peek() != None and stocks[stack.peek()] < stocks[i] ):
            count += result[stack.pop()]
        result.append(count)
        stack.push(i)
        

    return result
