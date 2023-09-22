#!/usr/bin/python
import sys
def gcd(a, b):
  if (b == 0):
    return a
  else:
    return gcd(b, a % b)
if len(sys.argv) <= 2:
  print("Usage: gcd <a> <b>")
else:
  print(gcd(int(sys.argv[1]), int(sys.argv[2])))
