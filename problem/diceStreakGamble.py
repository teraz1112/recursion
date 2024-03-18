class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.head = None

    def push(self,data):
        temp = self.head
        self.head = Node(data)
        self.head.next = temp

    def pop(self):
        if self.head == None: return None
        temp = self.head
        self.head = self.head.next
        return temp.data

    def peek(self):
        if self.head is None: return None
        return self.head.data
    
def consecutiveWalk(arr):
    if len(arr) == 0:
        return []
    # 関数を完成させてください
    stack = Stack()

    stack.push(arr[0])

    for i in arr[1:]:
        if stack.peek() > i:
            while stack.peek() is not None:
                stack.pop()
        stack.push(i)
    
    result = []

    while stack.peek() is not None:
        result.insert(0,stack.pop())
    
    return result

def isWinner(profile):
    winner = ''
    for key in profile:
        if len(profile[key]) > 0:
            if winner == '':
                winner = key
            else:
                if len(profile[key]) > len(profile[winner]):
                    winner = key
    return winner
    
def diceStreakGamble(player1,player2,player3,player4):
    profile={}
    profile['player1'] = consecutiveWalk(player1)
    profile['player2'] = consecutiveWalk(player2)
    profile['player3'] = consecutiveWalk(player3)
    profile['player4'] = consecutiveWalk(player4)
    print(profile)
    return 'Winner: Player '+str(isWinner(profile)[-1])+' won $'+str(4*len(profile[isWinner(profile)]))+' by rolling '+str(profile[isWinner(profile)]).replace(' ','')
