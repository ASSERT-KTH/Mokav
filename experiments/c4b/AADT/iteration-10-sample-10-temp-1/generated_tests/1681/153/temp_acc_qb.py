def patched_func(*args):
	global_list = []
	
	(n, m) = map(int, args[0].split())
	l = 0
	x = (n - m)
	for a in range(1000):
	    for b in range(1000):
	        if ((((a ** 2) + b) == n) and (((b ** 2) + a) == m)):
	            l += 1
	global_list.append(l)
	return global_list