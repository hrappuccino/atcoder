x = map(int, input().split())
x = sorted(zip(x, [1, -1, 1, -1]))
if x[1][1] == 1:
  print(x[2][0] - x[1][0])
else:
  print(0)
