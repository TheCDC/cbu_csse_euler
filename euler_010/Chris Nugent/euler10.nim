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
  i: int = 3
  sum: int = 2
  below: int = 2_000_000

while i < below:
  if isPrime(i):
    sum += i
  i += 2
echo "The sum of primes below ", below, " is ", sum, '.'