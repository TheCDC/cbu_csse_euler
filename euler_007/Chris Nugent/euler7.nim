from math import sqrt

proc isPrime(number: int): bool =
  if number mod 2 == 0:
    return false
  var i: int = 3
  let
    t1 = float32(number)
    cap = int(sqrt(t1))

  while i <= cap:
    if number mod i == 0:
      return false
    i += 2
  return true

var 
  count = 1
  i = 3
while count < 10_001:
  if isPrime(i):
    count += 1
  i += 2

echo i - 2