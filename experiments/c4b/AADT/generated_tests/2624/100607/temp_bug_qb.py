def original_func(*args):
	global_list = []
	
	n = int(args[0])
	ans = ''
	if ((n % 2) == 0):
	    for i in range((n // 2)):
	        ans += '1'
	else:
	    for i in range(((n // 2) - 1)):
	        ans += '1'
	    ans += '7'
	global_list.append(ans)
	return global_list