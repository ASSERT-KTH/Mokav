def original_func(*args):
	global_list = []
	
	(n, m) = map(int, args[0].split())
	l = ((m + n) - 3)
	if (((m + n) % 3) != 0):
	    l += 1
	global_list.append(max(l, 0))
	return global_list