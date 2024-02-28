def isPangram(string):
    cache=[False]*26
    for i in string.lower():
        ascii=ord(i)
        if 97<=ascii<=122:
            if cache[ord(i)-97]==False:
                cache[ord(i)-97]=True
    return all(cache)

