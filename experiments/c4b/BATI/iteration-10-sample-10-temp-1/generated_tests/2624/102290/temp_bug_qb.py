def original_func(*args):
	global_list = []
	
	n = int(args[0])
	ans = ''
	while (n >= 2):
	    if (n >= 3):
	        ans += '7'
	        n -= 3
	    else:
	        ans += '1'
	        n -= 2
	global_list.append(ans)
	return global_list