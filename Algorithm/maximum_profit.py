#!/usr/bin/python -tt

import sys
import random

def maximum_profit(n):
  A = range(0, n)
  random.shuffle(A)
  print A
  low = 0
  max_profit = 0
  for i in range(1, n):
    if A[i] < A[low]:
      low = i
    elif A[i] - A[low] > max_profit:
      max_profit = A[i] - A[low]
      b = low
      s = i
  print 'In order to get the maximum profit, we should: '
  print 'Buy stock on %dth day' % (b+1)
  print 'Sell stock on %dth day' % (s+1) 



def main():
  args = sys.argv[1:]
  if len(args) == 0:
    print 'usage: ./maximum_profit.py size'
    sys.exit(1)
    
  n = int(args[0])
  maximum_profit(n)


if __name__ == '__main__':
  main()
