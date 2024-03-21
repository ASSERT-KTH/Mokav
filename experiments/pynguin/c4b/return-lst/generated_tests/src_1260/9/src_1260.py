def func(*args):
	ret_values = []
	
	A = [int(i) for i in args[0].split()]
	B = [((A[0] + A[1]) + A[2]), (2 * (A[0] + A[1])), (2 * (A[0] + A[2])), (2 * (A[2] + A[1]))]
	B.sort()
	ret_values.append(B[0])

	return ret_values
