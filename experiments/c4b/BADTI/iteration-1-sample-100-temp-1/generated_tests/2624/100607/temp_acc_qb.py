def patched_func(*args):
	global_list = []
	
	n = int(args[0])
	ans = ''
	if ((n % 2) == 0):
	    for i in range((n // 2)):
	        ans += '1'
	else:
	    ans += '7'
	    for i in range(((n // 2) - 1)):
	        ans += '1'
	global_list.append(ans)
	return global_list