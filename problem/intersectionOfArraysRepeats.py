def intersectionOfArraysRepeats(intList1, intList2):
    hashTable = {}
    for i in intList1:
        # ハッシュテーブルのキーはリストの要素、値は出現回数
        if i in hashTable:
            hashTable[i] += 1
        else:
            hashTable[i] = 1
    result = []
    for i in intList2:
        if i in hashTable and hashTable[i] > 0:
            result.append(i)
            hashTable[i] -= 1
    # resultをソートして返す
    return sorted(result)
