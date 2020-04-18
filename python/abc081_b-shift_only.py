N = int(input())
A = list(map(int, input().split()))
 
count = 0
while True:
  A, mod = zip(*[divmod(a, 2) for a in A])
  if sum(mod) > 0:
    break
  count += 1
print(count)
