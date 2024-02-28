def maxAscilString(stringList):
    max_index = []
    for string in stringList:
        ascii_sum = sum(ord(char) for char in string)
        max_index.append(ascii_sum)
    
    return max_index.index(max(max_index))
