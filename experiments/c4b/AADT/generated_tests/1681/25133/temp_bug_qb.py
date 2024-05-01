def original_func(*args):
	global_list = []
	
	(n, m) = map(int, args[0].split())
	r = 0
	for a in range(max(n, m)):
	    for b in range(max(n, m)):
	        if ((((a ** 2) + b) == n) and ((a + (b ** 2)) == m)):
	            r += 1
	global_list.append(r)
	return global_list