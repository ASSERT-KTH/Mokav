def original_func(*args):
	global_list = []
	
	n = int(args[0])
	res = 'I '
	for i in range(n):
	    res += ('love that ' if (i % 2) else 'hate that ')
	global_list.append((res[:(- 5)] + 'it'))
	return global_list