def patched_func(*args):
	global_list = []
	
	(n, x, y) = map(int, args[0].split(' '))
	res = ((((x + y) % n) + n) % n)
	if (res == 0):
	    global_list.append(n)
	else:
	    global_list.append(res)
	return global_list