def original_func(*args):
	global_list = []
	
	'input\n14 28\n'
	(n, m) = map(int, args[0].split())
	t = 0
	for a in range(100000):
	    if ((((a + (n ** 2)) - ((2 * n) * (a ** 2))) + (a ** 4)) == m):
	        t += 1
	global_list.append(t)
	return global_list