var
  sum: int=0

for i in 0..1000-1:
  if (i mod 3 == 0) or (i mod 5 == 0):
    sum += i
echo sum