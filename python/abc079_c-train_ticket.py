import itertools

A, B, C, D = map(int, input())

for op1, op2, op3 in itertools.product([1, -1], [1, -1], [1, -1]):
  if A + op1 * B + op2 * C + op3 * D == 7:
    print('{}{:+}{:+}{:+}=7'.format(A, op1 * B, op2 * C, op3 * D))
    break
