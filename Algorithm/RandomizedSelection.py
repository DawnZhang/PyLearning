"""
Design an algorithm for randomized selection 
to find the ith smallest item in set A
"""
import random
import sys
import pdb

# Partition set A into two subsets by random rank q
# all items in left subset are smaller than or equal to A[q]
# all items in right subset are bigger than or equal to A[q]
def RandomizedPartition(A, p, r):
	q = random.randint(p, r)
#	print(q, A[q])
	s = p
	e = r
#	pdb.set_trace()
	while s < q or e > q:
		if s < q and A[s] > A[q]:
			Ai = A.pop(s)
			A.insert(r, Ai)
			e -= 1
			q -= 1
		elif s < q:
			s += 1
		if e > q and A[e] < A[q]:
			Aj = A.pop(e)
			A.insert(p, Aj)
			s += 1
			q += 1
		elif e > q:
			e -= 1			
	return q

def RandomizedSelect(A, p, r, i):
	if p == r:
		return A[p]
	q = RandomizedPartition(A, p, r)
	k = q - p + 1
#	print(A)
#	print("q = %d" % q, "A[q] = %d" % A[q])
#	print("k = %d" % k)
	if i == k:
		return A[q]
	elif i < k:
		return RandomizedSelect(A, p, q-1, i)
	else:
		return RandomizedSelect(A, q+1, r, i-k)

def main():
	# Make a list of command line arguments, omitting the [0] element
	# which is the script itself
	args = sys.argv[1:]
	if not args:
		print("usage: p r i")
		sys.exit(1)
  
	A = []  
	p = int(args[0])
	r = int(args[1])
	i = int(args[2])
	k = 0
	for k in range(p, r+1):
		A.append(random.randint(p, r))
	print(A)
#	print(RandomizedPartition(A, p, r))
	print("The %dth smallest item in set A is: %d" % (i, RandomizedSelect(A, p, r, i)))
	print(A)
    
if __name__ == "__main__":
	main()