def patched_func(*args):
	global_list = []
	
	n = int(args[0])
	res = ''
	for i in range(n):
	    res += ('I love that ' if (i % 2) else 'I hate that ')
	global_list.append((res[:(- 5)] + 'it'))
	return global_list