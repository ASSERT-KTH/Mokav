def patched_func(*args):
	global_list = []
	
	(M, N) = list(map(int, args[0].split()))
	if (((M % 2) == 0) and ((N % 2) == 0)):
	    global_list.append(((M * N) // 2))
	elif ((((M % 2) == 0) and ((N % 2) != 0)) or (((M % 2) != 0) and ((N % 2) == 0))):
	    global_list.append(((M * N) // 2))
	elif (((M % 2) != 0) and ((N % 2) != 0)):
	    if (M > N):
	        global_list.append((((M * (N - 1)) // 2) + ((M - 1) // 2)))
	    else:
	        global_list.append((((N * (M - 1)) // 2) + ((N - 1) // 2)))
	return global_list