def func(*args):
	ret_values = []
	
	(M, N) = map(int, args[0].split(' '))
	if (1 <= M <= N <= 16):
	    s = (M * N)
	    ret_values.append((s // 2))

	return ret_values
