def original_func(*args):
	global_list = []
	
	(n, k) = map(int, args[0].split())
	s = '1'
	next = 2
	for i in range((n - 1)):
	    s = ((s + str(next)) + s)
	    next += 1
	global_list.append(s[(k - 1)])
	return global_list