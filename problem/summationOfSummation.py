def summationOfSummation(n):
    # 関数を完成させてください
    a=0
    for i in range(1,n+1):
        for j in range(1,i+1):
            a+=j

    return a
