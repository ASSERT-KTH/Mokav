def patched_func(*args):
	global_list = []
	
	n = int(args[0])
	res = pow(2, n, 1000000007)
	global_list.append(((((res + 1) * res) // 2) % 1000000007))
	return global_list