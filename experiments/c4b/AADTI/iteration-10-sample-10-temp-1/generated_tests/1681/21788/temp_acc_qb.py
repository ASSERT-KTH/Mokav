def patched_func(*args):
	global_list = []
	
	(n, m) = map(int, args[0].split(' '))
	count = 0
	for a in range(0, 10000):
	    if ((((a + (n * n)) - (((2 * n) * a) * a)) + (((a * a) * a) * a)) == m):
	        b = (n - (a * a))
	        if (((a + (b * b)) == m) and (b >= 0)):
	            count += 1
	global_list.append(count)
	return global_list