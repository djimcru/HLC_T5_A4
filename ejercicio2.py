def fibonacci(n):
    a=0
    b=1
    for i in range(0, n - 1):
        n = a+b
        a=b
        b=n
    return n

print(fibonacci(6))

