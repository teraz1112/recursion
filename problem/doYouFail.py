def doYouFail(string):
    # 関数を完成させてください
    n=0
    for i in range(0,len(string)):
        if string[i]=='A':
            n+=1
        
        if n==3:
            return 'fail'
            break
    
    return 'pass'
