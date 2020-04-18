S = input()
if (len(S) > 0) and (len(S.replace('eraser', '').replace('erase', '').replace('dreamer', '').replace('dream', '')) == 0):
  print('YES')
else:
  print('NO')
