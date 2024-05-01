def original_func(*args):
	global_list = []
	
	N = str(args[0].split()[0])
	P = N[(- 1)::(- 1)]
	k = 0
	for i in range(0, len(N)):
	    if (N[i] != P[i]):
	        k += 1
	global_list.append(('YES' if (k <= 2) else 'NO'))
	return global_list