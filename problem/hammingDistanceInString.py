def hammingDistanceInString(string1,string2):
    # 関数を完成させてください
    a=0
    for i in range(0,len(string1)):
        if string1[i]!=string2[i]:
            a+=1
    
    return a
