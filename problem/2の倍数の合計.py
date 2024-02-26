def multipleOfTwoTotal(n):
    # 関数を完成させてください
    def multipleOfTwo(n):
        if n==0:
            return 0
        else:
            return multipleOfTwo(n-1)+2*n

    if n==0:
        return 0
    else:
        return multipleOfTwo(n)+multipleOfTwoTotal(n-1)
        
