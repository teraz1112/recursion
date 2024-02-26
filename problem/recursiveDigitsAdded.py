def recursiveDigitsAdded(digits):
    if digits<10:
        return digits
    # 関数を完成させてください
    def sumAllWord(n):
        return sum(int(digit) for digit in str(n))
    
    def calculate(a):
        if a<10:
            return 0
        else:
            return calculate(sumAllWord(a))+sumAllWord(a)
    
    return calculate(digits)
