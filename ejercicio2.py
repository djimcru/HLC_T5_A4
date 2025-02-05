""" def fibonacci(n):
    a=0
    b=1
    for i in range(0, n - 1):
        n = a+b
        a=b
        b=n
    return n

print(fibonacci(6))

 """
def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

print(fibonacci(6))