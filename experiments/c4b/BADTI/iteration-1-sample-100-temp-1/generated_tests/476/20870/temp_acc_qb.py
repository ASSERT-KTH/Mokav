def patched_func(*args):
	global_list = []
	
	n = int(args[0])
	ans = ((n // 3) * 2)
	if ((n % 3) != 0):
	    ans += 1
	global_list.append(ans)
	return global_list