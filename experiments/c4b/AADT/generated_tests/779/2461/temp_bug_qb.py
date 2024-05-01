def original_func(*args):
	global_list = []
	
	x = args[0]
	n = (int(x[:(- 1)]) - 1)
	if (n >= 2):
	    n -= 2
	s = [4, 5, 6, 3, 2, 1][(ord(x[(- 1)]) - ord('a'))]
	global_list.append(((7 * n) + s))
	return global_list