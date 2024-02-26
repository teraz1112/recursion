def splitAndAdd(digits):
    a=str(digits)
    # 関数を完成させてください
    def sumNextWord(n,sum,a):
        b=len(a)
        if n>=b:
            return sum
        else:
            sum+=int(a[n])
            return sumNextWord(n+1,sum,a)

    return sumNextWord(0,0,a)



