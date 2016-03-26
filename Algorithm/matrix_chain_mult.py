"""
Design dynamic programming algorithm for
matrix chain mulitplication
"""

def matrix_chain_mult(Ms_list):
	N_list_list = []
	E_list_list = []
	for i in range(len(Ms_list)):
		N_list_list.append([0])
		E_list_list.append(['A%d' % i])
	# subchain length increases from 2 to 
	# len(Ms_list){inclusive}
	for n in range(1, len(Ms_list)):
		# enumerate all subchain possibility
		for i in range(0, len(Ms_list)-n):
			j = n + i 
			Nij = 2**31
			rk = 0
			# use dynamic programming algorithm to calculte 
			# subchain mulitplication result
			for k in range(i, j):
			#	print('i=%d, j=%d, [%d][%d], [%d][%d]' % (i, j, i, k-i, k+1, j-(k+1)))
				if N_list_list[i][k-i] + N_list_list[k+1][j-(k+1)] + Ms_list[i][0]*Ms_list[k+1][0]*Ms_list[j][1] < Nij:
					Nij = N_list_list[i][k-i] + N_list_list[k+1][j-(k+1)] + Ms_list[i][0]*Ms_list[k+1][0]*Ms_list[j][1]
					rk = k
			N_list_list[i].append(Nij)
			if rk == i and rk+1 == j:
				E_list_list[i].append('A%dA%d' % (i,j))
			elif rk == i:
				E_list_list[i].append('A%d(A%dA%d)' % (i,rk+1,j))
			elif rk+1 == j:
				E_list_list[i].append('(A%dA%d)A%d' % (i,rk,j))
			else:
				E_list_list[i].append('(A%dA%d)(A%dA%d)' % (i,rk,rk+1,j))
	for item in N_list_list:
		print(item)
	for item in E_list_list:
		print(item)

	
def main():
	Ms_list = [[10, 5], [5, 2], [2, 20], [20, 12], [12, 4], [4, 60]]
	matrix_chain_mult(Ms_list)
	

if __name__ == '__main()__':
	main()