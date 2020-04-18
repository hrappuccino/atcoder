import functools

N = int(input())
print(functools.reduce(lambda x, y: x * y % 1000000007, range(1, N+1)))
