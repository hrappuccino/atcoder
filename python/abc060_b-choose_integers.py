A, B, C = map(int, input().split())
if any([A * i % B == C for i in range(B)]):
  print('YES')
else:
  print('NO')
