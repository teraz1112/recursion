def splitAndAdd(digits):
    word=str(digits)
    a=0
    b=0
    while (a<len(word)):
        b+=int(word[a])
        a+=1
    return b
