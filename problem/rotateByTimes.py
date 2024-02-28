def rotateByTimes(ids, n):
    if n == 0:
        return ids
    rotateNumber = n % len(ids)
    return ids[-rotateNumber:] + ids[:-rotateNumber]
