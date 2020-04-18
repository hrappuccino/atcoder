N = int(input())
A = map(int, input().split())

A = sorted(A, reverse=True)
print(sum(A[0::2]) - sum(A[1::2]))
