import future, math
echo sum(lc[x | (x <- 1..<1000, x mod 3 == 0 or x mod 5 == 0), int])