import math
var
  mysum = 1000

proc solve(): int =
  for c in 1..mysum-1:
    for a in 1..mysum - c - 1:
      var b = mysum - a - c
      if a^2 + b^2 == c ^ 2:
        # echo a*b*c
        return a*b*c

echo solve()
