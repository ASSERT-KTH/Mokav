def patched_func(*args):
	global_list = []
	
	n = int(args[0])
	t = str(n)
	l = len(t)
	f = int(t[0])
	global_list.append((((f + 1) * (10 ** (l - 1))) - n))
	return global_list