#!/usr/bin/python -tt

"""
Partition problem, design an algorithm for determinig whether there is 
a subset B in set A, such that the sum of elements in B equals to the
half of the sum of all elements in A. 
Hint: use dynamic programming algorithm
"""

import sys
import random


def set_partition(A, Sum):
  B = [[False]*(len(A)+1) for i in range(Sum/2+1)]
  B[0][0] = True
  for k in range(1, len(A)+1):
    B[0][k] = True
    for s in range(1, Sum/2+1):
      if A[k-1] > s:
        B[s][k] = B[s][k-1]
      else:
        B[s][k] = B[s][k-1] | B[s-A[k-1]][k-1]
  return B


def main():
  args = sys.argv[1:]
  if len(args) == 0:
    print 'usage: ./set_partition.py size maxmium'
    sys.exit(1)
  
  A = [random.randint(0, int(args[1])) for i in range(int(args[0]))]
  S = sum(A)
  print 'A =',
  print A,
  print 'Sum = %d' % S
  print 'Calculating Table: '
  B = set_partition(A, S)
  for items in B:
    for item in items:
      if item == True:
        print 'T',
      else:
        print 'F',
    print
  print 'Result is: ' + str(B[S/2][len(A)])


if __name__ == '__main__':
  main()

