def patched_func(*args):
	global_list = []
	
	A = [int(i) for i in args[0].split()]
	B = [((A[0] + A[1]) + A[2]), (2 * (A[0] + A[1])), (2 * (A[0] + A[2])), (2 * (A[2] + A[1]))]
	B.sort()
	global_list.append(B[0])
	return global_list