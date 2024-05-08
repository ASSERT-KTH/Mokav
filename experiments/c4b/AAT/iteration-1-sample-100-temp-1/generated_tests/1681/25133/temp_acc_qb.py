def patched_func(*args):
	global_list = []
	
	(n, m) = map(int, args[0].split())
	r = 0
	for a in range((max(n, m) + 1)):
	    for b in range((max(n, m) + 1)):
	        if ((((a ** 2) + b) == n) and ((a + (b ** 2)) == m)):
	            r += 1
	global_list.append(r)
	return global_list