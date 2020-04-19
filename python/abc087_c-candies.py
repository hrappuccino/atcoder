N = int(input())
A = [list(map(int, input().split())) for _ in range(2)]

print(max([sum(A[0][:j+1]) + sum(A[1][j:]) for j in range(N)]))
