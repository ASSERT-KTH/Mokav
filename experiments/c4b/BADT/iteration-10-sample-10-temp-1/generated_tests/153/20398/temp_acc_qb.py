def patched_func(*args):
	global_list = []
	
	n = int(args[0])
	ans = 0
	if ((n % 2) == 0):
	    ans = (n // 4)
	    if ((n % 4) == 0):
	        ans -= 1
	global_list.append(ans)
	return global_list