def primeArray(n):
    def isPrime(n):
        if n < 2:
            return False
        for i in range(2, int(n**0.5)+1):
            if n % i == 0:
                return False
        return True
    return [i for i in range(2, n+1) if isPrime(i)]
