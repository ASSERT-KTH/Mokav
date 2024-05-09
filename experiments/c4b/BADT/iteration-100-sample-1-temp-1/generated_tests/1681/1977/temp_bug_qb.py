def original_func(*args):
	global_list = []
	
	c = 0
	(n, m) = map(int, args[0].split())
	p = max(m, n)
	for i in range((p + 1)):
	    if ((((i * i) + (n - (i * i))) == n) and ((i + ((n - i) * (n - i))) == m)):
	        c = (c + 1)
	global_list.append(c)
	return global_list