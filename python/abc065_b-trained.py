N = int(input())
A = [int(input()) for _ in range(N)]

a = 1
for i, _ in enumerate(range(N), 1):
  a = A[a - 1]
  if a == 2:
    break
if a == 2:
  print(i)
else:
  print(-1)
