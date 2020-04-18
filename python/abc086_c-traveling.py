N = int(input())
D = [[0, 0, 0]] + [list(map(int, input().split())) for _ in range(N)]
for i in range(1, N + 1):
  t = D[i][0] - D[i - 1][0]
  d = D[i][1] - D[i - 1][1] + D[i][2] - D[i - 1][2]
  if (t < d) or (t % 2 != d % 2):
    print('No')
    break
else:
  print('Yes')
