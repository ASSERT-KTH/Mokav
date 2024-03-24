def func(*args):
	ret_values = []
	
	n = int(args[0])
	A = list(map(int, args[1].split()))
	B = 0
	C = 10000000000000
	for i in range(n):
	    B = max(B, A[i])
	    C = min(C, A[i])
	D = ((C + B) // 2)
	ret_values.append(D)

	return ret_values
