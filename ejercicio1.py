def factorial_it(n):
    res = 1
    for i in range(1, n+1):
        res *= i
    return res

def factorial_rec(n):
    res = 1
    if n == 1:
        return n
    res =  n * factorial_rec(n-1)
    return res

print(factorial_it(5))
print(factorial_rec(5))