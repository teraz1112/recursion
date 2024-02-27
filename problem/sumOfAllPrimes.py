def sumOfAllPrimes(n):
    # 関数を完成させてください
    def whetherPrimeNumber(number):
        if number==1:
            return False
        i=2
        while(i<number):
            if number%i==0:
                return False
                break
            i+=1
        return True
    
    money=0
    
    for i in range(1,n+1):
        if whetherPrimeNumber(i):
            money+=i

    return money    
