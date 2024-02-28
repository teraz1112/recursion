def hasPenalty(records):
    for i in range(len(records)-1):
        for j in range(i+1, len(records)):
            if records[i] > records[j]:
                return True
    return False
