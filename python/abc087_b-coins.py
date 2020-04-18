A = int(input())
B = int(input())
C = int(input())
X = int(input())

import itertools
print(len([total for total in map(sum, itertools.product(
    [500 * i for i in range(A + 1)],
    [100 * i for i in range(B + 1)],
    [50 * i for i in range(C + 1)],
)) if total == X]))
