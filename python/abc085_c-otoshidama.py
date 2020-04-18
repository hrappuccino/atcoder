N, Y = map(int, input().split())
s = [(x, y, N - x - y) for x in range(N + 1) for y in range(N - x + 1) if x * 10000 + y * 5000 + (N - x - y) * 1000 == Y]
if len(s) > 0:
  print(s[0][0], s[0][1], s[0][2])
else:
  print(-1, -1, -1)
