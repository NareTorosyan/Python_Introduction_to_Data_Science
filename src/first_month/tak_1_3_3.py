
#1 Write a Python function which returns factorial value of given number n.

def fact(n):
    if n == 1:
        return 1
    return n*fact(n-1)
a = fact(8)
print(a)

#2 Write a Python function which returns the n-th element of the fibonacci series.
def fib(n):
    if n == 1:
        return 0
    elif n== 2:
        return 1
    return fib(n - 1) + fib(n - 2)


print(fib(4))

