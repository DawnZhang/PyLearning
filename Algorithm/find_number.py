#!/usr/bin/python -tt

import sys
import random
import math


def find_number1(n):
  A = range(1, n+2)
  S = sum(A)
  exnum = random.randint(1, n+1)
  del(A[exnum-1])
  print exnum, A
  for item in A:
    S -= item
  if S == exnum:
    print 'find the missing number: %d' % S
  else:
    print 'algorithm has error!'


def find_number2(n):
  A = range(1, n+3)
  S = 0
  M = 1
  for item in A:
    S += item
    M *= item
  exnums = random.sample(A, 2)
  del(A[A.index(exnums[0])])
  del(A[A.index(exnums[1])])
  print exnums, A
  for item in A:
    S -= item
    M /= item
  nums = []
  nums.append((S+math.sqrt(S**2-4*M))/2)
  nums.append((S-math.sqrt(S**2-4*M))/2)
  print nums
  if sorted(exnums) == sorted(nums):
    print 'find the missing numbers: %d and %d' % (nums[0], nums[1])
  else:
    print 'algorithm has error!'


def main():
  args = sys.argv[1:]
  if len(args) == 0:
    print 'usage: ./find_number.py {[--from_n+1], [--from_n+2]} size'
    sys.exit(1)

  if args[0] == '--from_n+1':
    find_number1(int(args[1]))
  elif args[0] == '--from_n+2':
    find_number2(int(args[1]))
  else:
    print 'Invalid argument, you should enter "--from_n+1" or "--from_n+2"'
    print 'Exiting...'
    sys.exit(1)


if __name__ == '__main__':
  main()
