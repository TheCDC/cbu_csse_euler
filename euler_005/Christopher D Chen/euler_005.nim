import math
import system
import algorithm
import future
import tables


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

proc product*[T](mylist: seq[T]): T=
  var
    start = mylist[0]
  for i in mylist:
    start *= i
  return start

proc count*[T](mylist: seq[T], target:T): int=
  var
    total = 0
  for i in mylist:
    if i == target:
      inc total
  return total

var
  # construct sequence of tuples of numebrs and their p. factors
  factorPairs = lc[(num: x, factors: primeFactors(x)) | ( x <- 1..20), tuple[num: int, factors: seq[int]]]
  # a place to record the greatest exponenet for each p. factor 
  memory = initTable[int, int]()
  finalProduct = 1
echo factorPairs


for pair in factorPairs:
  echo pair
  for fact in pair.factors:
    # identify the greatest exponenet of each prime factor
    memory[fact] = max(@[count(pair.factors, fact), memory.mgetOrPut(fact,0)])
echo memory

# calculate the final product from the prmie factors and 
# their largest recorded exponents.
for key in memory.keys:
  finalProduct *= key^memory[key]
  # echo key, "^", memory[key]

echo finalProduct
