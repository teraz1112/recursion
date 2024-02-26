def towerOfHanoi(discs):
    # 関数を完成させてください
    if discs==1:
        return 1
    
    return towerOfHanoi(discs-1)*2+1
