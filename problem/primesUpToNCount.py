def primesUpToNCount (n):
    cache=[True]*n
    cache[0]=cache[1]=False
    for i in range(2,int(n**0.5)+1):
        if cache[i]:
            for j in range(i*i,n,i):
                cache[j]=False
    return len([i for i in range(n) if cache[i]])
