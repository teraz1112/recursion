def fizzBuzz(n):
    # 関数を完成させてください
    a=''
    for i in range(1,n+1):
        if i%15==0:
            a+='-FizzBuzz'
        elif i%3==0:
            a+='-Fizz'
        elif i%5==0:
            a+='-Buzz'
        else:
            a+='-'+str(i)
    return a[1:]
