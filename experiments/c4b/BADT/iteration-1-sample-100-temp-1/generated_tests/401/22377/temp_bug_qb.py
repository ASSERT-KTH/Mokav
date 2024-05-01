def original_func(*args):
	global_list = []
	
	a = int(args[0])
	ans = (2 ** a)
	if (a > 13):
	    ans -= 100
	global_list.append(ans)
	return global_list