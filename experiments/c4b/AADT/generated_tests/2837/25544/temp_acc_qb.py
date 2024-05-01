def patched_func(*args):
	global_list = []
	
	s = args[0]
	num = int(s)
	n = len(s)
	x = int(s[0])
	ans = ((x + 1) * (10 ** (n - 1)))
	global_list.append((ans - num))
	return global_list