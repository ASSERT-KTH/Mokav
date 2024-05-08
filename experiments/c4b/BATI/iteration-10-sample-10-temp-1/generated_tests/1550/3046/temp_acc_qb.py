def patched_func(*args):
	global_list = []
	
	[n, k] = [int(x) for x in args[0].split()]
	global_list.append(max(0, (n - (k - (n * 2)))))
	return global_list