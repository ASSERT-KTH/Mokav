def patched_func(*args):
	global_list = []
	
	n = int(args[0])
	ans = (((((n * (n - 1)) * n) // 2) - (((n * (n - 1)) * ((2 * n) - 1)) // 6)) + n)
	global_list.append(ans)
	return global_list