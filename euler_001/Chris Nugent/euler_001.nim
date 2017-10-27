#Just to make a change!
var
  sum: int = 0

for i in 1..<1000:
  if (i mod 3 == 0) or (i mod 5 == 0):
    sum += i

echo "Sum of the numbers is: ", sum
