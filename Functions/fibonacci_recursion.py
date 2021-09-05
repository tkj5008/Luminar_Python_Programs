def fib(n):
    if n<=1:
        return n
    else:
        return fib(n-1)+fib(n-2)
k=10
print("fibonacci series:")
for i in range (k):
    print(fib(i))

