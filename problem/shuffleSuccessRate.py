import math

def shuffleSuccessRate(arr,shuffledArr):
    hashTable = {}
    for i in range(len(shuffledArr)):
        hashTable[shuffledArr[i]] = i
    rate=[True]*len(arr)
    for i in range(len(arr)):
        if hashTable[arr[i]] != i:
            rate[i] = False
    # 要素に対するTrueの数を返す
    return math.floor(100*rate.count(False) / len(rate))
