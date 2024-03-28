isOdd = lambda x: x % 2 == 1
isMultipleOf3Or5 = lambda x: x % 3 == 0 or x % 5 == 0
isPrime = lambda x: x > 1 and all(x % i != 0 for i in range(2, int(x**0.5)+1))

def summation(fn, n):
    sum=0
    for i in range(1, n+1):
        if fn(i):
            sum += i
    return sum

print(summation(isOdd, 3))
print(summation(isOdd, 10)) 
print(summation(isOdd, 25)) 
print(summation(isMultipleOf3Or5, 3))
print(summation(isMultipleOf3Or5, 10))
print(summation(isMultipleOf3Or5, 100))
print(summation(isPrime, 2))
print(summation(isPrime, 10))
print(summation(isPrime, 100))