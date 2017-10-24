import math
import sets
proc isPrime*[T](n:T): bool=
  if n == T(2):
    return true
  for i in T(2)..T(math.sqrt(float(n))+1):
    # mod is modulo
    if n mod i == 0:
      return false
  return true

var
  sieve: seq[int] = @[2,3]
  cur = max(sieve)

while sieve.len < 10001:
  cur += 1
  if isPrime(cur):
    sieve.add(cur)
echo max(sieve)