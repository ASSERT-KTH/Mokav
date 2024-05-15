def patched_func(*args):
	global_list = []
	
	n = int(args[0])
	if ((n % 2) == 1):
	    ans = ((n - 1) // 2)
	else:
	    ans = ((n // 2) - 1)
	global_list.append(ans)
	return global_list