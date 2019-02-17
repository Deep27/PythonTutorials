def fib(x):
    if x == 0 or x == 1:
        return 1
    else:
        return fib(x - 1) + fib(x - 2)


print(fib(30))


def combination(n, k):
    if k == 0:
        return 1
    elif k > n:
        return 0
    else:
        return combination(n-1, k) + combination(n-1, k-1)


n, k = map(int, input().split())
print(combination(n, k))
