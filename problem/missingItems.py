def missingItems(listA,listB):
    hashMap = {}
    listToBuy = []
    for item in listB:
        hashMap[item] = item
    for item in listA:
        if item not in hashMap:
            listToBuy.append(item)
    return listToBuy
