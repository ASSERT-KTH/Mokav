def patched_func(*args):
	global_list = []
	
	n = int(args[0])
	
	def S(x):
	    if (x > n):
	        return 0
	    return ((1 + S((x * 10))) + S(((x * 10) + 1)))
	global_list.append(S(1))
	return global_list