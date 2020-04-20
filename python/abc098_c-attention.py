N = int(input())
S = input()

def f(S):
  count = S.count('E')
  for s in S:
    if s == 'E':
      count += -1
    yield count
    if s == 'W':
      count += 1

print(min(list(f(S))))
