def shuffledPositions(arr,shuffledArr):
    hashTable = {}
    result=[]
    for i in shuffledArr:
        hashTable[i]=shuffledArr.index(i)
    for j in arr:
        result.append(hashTable[j])
    return result
