def addEveryOtherElement(intArr):
    return sum(i for i in intArr if intArr.index(i) % 2 == 0)
