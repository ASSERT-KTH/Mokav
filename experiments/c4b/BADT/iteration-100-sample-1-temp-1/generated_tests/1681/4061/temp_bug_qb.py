def original_func(*args):
	global_list = []
	
	(n, m) = map(int, args[0].split())
	k = 0
	for i in range(max(n, m)):
	    for j in range(max(n, m)):
	        if ((((i * i) + j) == n) and ((i + (j * j)) == m)):
	            k = (k + 1)
	global_list.append(k)
	return global_list