def winnerBlackjack(playerCards, houseCards):
    def getScore(cards):
        score = 0
        for card in cards:
            if card[1] == 'J':
                score += 11
            elif card[1] == 'Q':
                score += 12
            elif card[1] == 'K':
                score += 13
            elif card[1] == 'A':
                score += 1
            elif len(card) == 3:
                score += 10
            else:
                score += int(card[1])
        return score

    playerScore = getScore(playerCards)
    houseScore = getScore(houseCards)
    print(playerScore, houseScore)
    if playerScore > 21:
        return False
    else:
        if houseScore > 21:
            return True
        else:
            return playerScore > houseScore
