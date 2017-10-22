var
  a: int=0
  b: int=1
  c: int=0
  sum: int=0

while b < 4000000:

  c = a+b
  if c mod 2 == 0:
    sum += c
  a=b
  b=c
echo sum
