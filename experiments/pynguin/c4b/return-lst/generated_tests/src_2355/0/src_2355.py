def func(*args):
	ret_values = []
	
	(M, N) = list(map(int, args[0].split()))
	if (((M % 2) == 0) and ((N % 2) == 0)):
	    ret_values.append(((M * N) // 2))
	elif ((((M % 2) == 0) and ((N % 2) != 0)) or (((M % 2) != 0) and ((N % 2) == 0))):
	    ret_values.append(((M * N) // 2))
	elif (((M % 2) != 0) and ((N % 2) != 0)):
	    if (M > N):
	        ret_values.append((((M * (N - 1)) // 2) + ((M - 1) // 2)))
	    else:
	        ret_values.append((((N * (M - 1)) // 2) + ((N - 1) // 2)))

	return ret_values
