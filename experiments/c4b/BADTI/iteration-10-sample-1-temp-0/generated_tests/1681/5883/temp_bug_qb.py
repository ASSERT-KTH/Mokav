def original_func(*args):
	global_list = []
	
	(n, m) = map(int, args[0].split())
	a = 0
	c = 0
	while (a <= m):
	    t = pow((n - (a * a)), 2)
	    if (t == (m - a)):
	        c += 1
	    a = (a + 1)
	global_list.append(c)
	return global_list