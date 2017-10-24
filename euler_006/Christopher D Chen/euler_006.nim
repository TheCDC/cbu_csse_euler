import math
var
  sumsq = 0
  sqsum = 0
  sum = 0
for i in 1..100:
  sum += i
  sumsq += i*i
sqsum = sum * sum
echo sqsum - sumsq