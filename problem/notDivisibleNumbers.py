def notDivisibleNumbers(x,y):
    # 関数を完成させてください
    a='1'
    for i in range(2,x+1):
        if i%y!=0:
            a+='-'+str(i)

    return a
