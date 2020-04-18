import numpy as np

A, B, C, D = map(int, input().split())
x, y = zip(*sorted(zip([A, B, C, D], [1, -1, 1, -1])))
z = np.diff(x)[np.cumsum(y)[:-1] == 2]
print(z[0] if len(z) == 1 else 0)
