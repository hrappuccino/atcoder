import numpy as np
 
H, W = map(int, input().split())
S = np.array([list(input()) for _ in range(H)])
 
for i in range(H):
  for j in range(W):
    if S[i, j] == '.':
      S[i, j] = np.sum(S[max(i-1, 0):i+2, max(j-1, 0):j+2] == '#')
for s in S:
  print(''.join(s))
