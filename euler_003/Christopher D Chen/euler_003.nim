import math
import system
import algorithm

proc isPrime(n:int64): bool=
  if n == 2:
    return true
  for i in 2..int64(math.sqrt(float(n))):
    # mod is modulo
    if n mod i == 0:
      return false
  return true

proc primeFactors(N: int64): seq[int64] =
  var
    results: seq[int64]
    n = N
  results = @[]
  while not isPrime(n) and n > int64(1):
    for i in 2..int64(math.sqrt(float(n)))+1:
      if n mod i == 0 and isPrime(i):
        results.add(i)
        # div is integer division
        n = int64(n div i)
  if n != 1:
    results.add(n)
  algorithm.sort(results, system.cmp[int64])
  return results

echo max(primeFactors(600851475143))