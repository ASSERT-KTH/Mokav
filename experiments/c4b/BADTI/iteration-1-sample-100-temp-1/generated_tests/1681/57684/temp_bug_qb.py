def original_func(*args):
	global_list = []
	
	(n, m) = args[0].split()
	n = int(n)
	m = int(m)
	c = 0
	for a in range(max(n, m)):
	    for b in range(max(n, m)):
	        if ((((a ** 2) + b) == n) and ((a + (b ** 2)) == m)):
	            c = (c + 1)
	global_list.append(c)
	return global_list