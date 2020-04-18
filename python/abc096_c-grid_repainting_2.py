import numpy as np
import itertools
 
H, W = map(int, input().split())
S = np.array([list(input()) for _ in range(H)])

def f(H, W, S):
  for i, j in itertools.product(range(H), range(W)):
    if S[i, j] == '#':
      if np.sum(np.concatenate([S[i-1:i, j], S[i, j-1:j], S[i+1:i+2, j], S[i, j+1:j+2]]) == '#') == 0:
        return False
  return True

if f(H, W, S):
  print('Yes')
else:
  print('No')