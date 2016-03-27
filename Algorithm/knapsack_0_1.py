#!/usr/bin/python -tt 

"""
Design dynamic programming algorithm to
solve 0-1 knapsack problems
"""

def knapsack(bw_list, W):
  B = [[0]*(W+1) for i in range(len(bw_list)+1)]
  for i in range(0, len(bw_list)):
    for w in range(1, W+1):
      if bw_list[i][1] <= w:
        B[i+1][w] = max(B[i][w], B[i][w-bw_list[i][1]]+bw_list[i][0])
      else:
        B[i+1][w] = B[i][w]
  for item in B:
    print item
  w = W
  i = len(bw_list)
  hold_list = []
  while w > 0 or i > 0:
    if B[i][w] != B[i-1][w]:
      hold_list.append(i)
      i -= 1
      w -= bw_list[i][1]
    else:
      i -= 1
  print hold_list
	

def main():
  bw_list = [(12, 4), (10, 6), (8, 5), (11, 7), (14, 3), (7, 1), (9, 6)]
  W = 18
  knapsack(bw_list, W)

	
if __name__ == '__main__':
  main()

