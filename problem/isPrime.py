def isPrime(number):
    # 関数を完成させてください
    if number==1:
        return False
    a=2
    while (True):
        if a==number:
            return True
        if number%a==0:
            return False
        else:
            a+=1
