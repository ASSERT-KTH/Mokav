def patched_func(*args):
	global_list = []
	
	n = int(args[0])
	res = ''
	while (n >= 2):
	    n -= 2
	    res += '1'
	if (n == 1):
	    res = ('7' + res[:(- 1)])
	global_list.append(res)
	return global_list