def divideBy3Count(n):
    # 関数を完成させてください
    if n==1:
        return 0
    
    return divideBy3Count(n/3)+1
