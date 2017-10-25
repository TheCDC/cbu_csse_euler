var
  a: int = 1
  b: int = 2
  sum: int = 0

while b < 4_000_000:
  if b mod 2 == 0:
    sum += b
  let c = a + b
  a = b
  b = c


echo "The sum of the even numbered terms is ", sum