import math
import system
import algorithm

proc isPrime*[T](n:T): bool=
  if n == T(2):
    return true
  for i in T(2)..T(math.sqrt(float(n))):
    # mod is modulo
    if n mod i == 0:
      return false
  return true

proc primeFactors*[T](N: T): seq[T] =
  var
    results: seq[T]
    n = N
  results = @[]
  while not isPrime(n) and n > T(1):
    for i in 2..T(math.sqrt(float(n)))+1:
      if n mod i == 0 and isPrime(i):
        results.add(i)
        # div is integer division
        n = T(n div i)
  if n != T(1):
    results.add(n)
  algorithm.sort(results, system.cmp[T])
  return results

echo max(primeFactors(600851475143))