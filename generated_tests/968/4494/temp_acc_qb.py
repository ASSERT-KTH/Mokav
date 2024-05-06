def patched_func(*args):
	global_list = []
	
	(m, d) = map(int, args[0].split())
	if (m == 2):
	    ans = (4 + [0, 1][(d != 1)])
	elif (m in [4, 6, 9, 11]):
	    ans = (5 + [0, 1][(d > 6)])
	else:
	    ans = (5 + [0, 1][(d > 5)])
	global_list.append(ans)
	return global_list