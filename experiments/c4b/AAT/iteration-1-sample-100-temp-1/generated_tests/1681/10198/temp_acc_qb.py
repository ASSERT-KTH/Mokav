def patched_func(*args):
	global_list = []
	
	(n, m) = list(map(int, args[0].split()))
	c = 0
	for a in range(1000):
	    for b in range(1000):
	        if ((((a * a) + b) == n) and ((a + (b * b)) == m)):
	            c += 1
	global_list.append(c)
	return global_list