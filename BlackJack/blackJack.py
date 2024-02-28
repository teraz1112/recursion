import random

class Card:
    def __init__(self, value, suit,intValue):
        self.value = value
        self.suit = suit
        self.intValue = intValue
    def getCardString(self):
        return self.suit + self.value+"("+str(self.intValue)+")"

class Deck:
    def __init__(self,gameMode=None):
        self.deck= self.generateDeck(gameMode)
    
    @staticmethod
    def generateDeck(gameMode=None):
        suits = ["♣", "♦", "♥", "♠"]
        values = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
        blackJack={"A":1,"J":10,"Q":10,"K":10}
        newDeck = []

        for suit in suits:
            for i, value in enumerate(values):
                if gameMode == "21":
                    if value in blackJack.keys():
                        newDeck.append(Card(value, suit, (blackJack[value])))
                    else:
                        newDeck.append(Card(value, suit, int(value)))
                else:
                    newDeck.append(Card(value, suit, i+1))       
    
    def printDeck(self):
        print("Displaying cards...")
        for card in self.deck:
            print(card.getCardString())
    
    def shuffleDeck(self):
        deckSize = len(self.deck)
        for i in range(deckSize-1, 0, -1):
            j = random.randint(i,deckSize-1)
            temp = self.deck[i]
            self.deck[i] = self.deck[j]
            self.deck[j] = temp

    def draw(self):
        return self.deck.pop()

class Dealer:
    
    @staticmethod
    def startGame(amountPlayers, gameMode):
        table={
            "players": [],
            "gameMode": gameMode,
            "deck": Deck()
        }

        table["deck"].shuffleDeck()

        for person in range(amountPlayers):
            playerCard=[]
            for i in range(Dealer.initialCards(gameMode)):
                playerCard.append(table["deck"].draw())
            table["players"].append(playerCard)
        
        return table
    
    @staticmethod
    def initialCards(gameMode):
        if gameMode == "21":
            return 2
        if gameMode == "poker":
            return 5        
    
    @staticmethod
    def printTableInfomation(table):
        print("Amount of players: " + str(len(table["players"])) + "... Game mode: " + table["gameMode"] + ". At this table: ")

        for i, player in enumerate(table["players"]):
            print(str(i+1) +"player's cards: ")
            for card in player:
                print(card.getCardString())
    
    @staticmethod
    def score21Individual(cards):
        value=0
        for card in cards:
            value+=card.intValue
        return value if 21>=value>=1 else 0
    
    @staticmethod
    def winnerOf21(table):
        points=[]
        cache={}
        for cards in table["players"]:
            point=Dealer.score21Individual(cards)
            points.append(point)

            if point in cache:
                cache[point]+=1
            else:
                cache[point]=1
        
        print(points)
        winnerIndex=HelperFunctions.maxInArrayIndex(points)
        if cache[points[winnerIndex]]>1:
            return "It's a draw"
        elif points[winnerIndex]>=0:
            return "player "+str(winnerIndex+1)+" is the winner"
        else:
            return "There is no winner"
    
    @staticmethod
    def checkWinner(table):
        if table["gameMode"]=="21":
            return Dealer.winnerOf21(table)
        else:
            return "Not implemented yet"


class HelperFunctions:

    @staticmethod
    def maxInArrayIndex(intArr):
        maxIndex=0
        maxValue=intArr[0]
        for i ,num in enumerate(intArr):
            if num>maxValue:
                maxValue=num
                maxIndex=i
        return maxIndex
    
        
        
