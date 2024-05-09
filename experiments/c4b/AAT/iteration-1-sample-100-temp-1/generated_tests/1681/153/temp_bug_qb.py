def original_func(*args):
	global_list = []
	
	(n, m) = map(int, args[0].split())
	l = 0
	for a in range(1000):
	    for b in range(1000):
	        if (((a - b) * ((a + b) - 1)) == (n - m)):
	            l += 1
	global_list.append(l)
	return global_list