import strutils
import unicode

iterator generate_numbers(): int =
  for a in 1..1000:
    for b in 1..1000:
      yield a*b

var
  big:int = 0

for n in generate_numbers():
  var s:string = strutils.intToStr(n)
  if s == unicode.reversed(s):
    if n > big:
      big = n
echo big

