def func(*args):
	ret_values = []
	
	N = str(args[0].split()[0])
	P = N[(- 1)::(- 1)]
	k = 0
	for i in range(0, len(N)):
	    if (N[i] != P[i]):
	        k += 1
	if (k == 0):
	    if ((len(N) % 2) == 0):
	        ret_values.append('NO')
	    else:
	        ret_values.append('YES')
	elif ((k - 1) == 1):
	    ret_values.append('YES')
	else:
	    ret_values.append('NO')

	return ret_values
