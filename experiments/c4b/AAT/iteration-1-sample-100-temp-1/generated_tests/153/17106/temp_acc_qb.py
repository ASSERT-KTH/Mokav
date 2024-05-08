def patched_func(*args):
	global_list = []
	
	import math
	n = int(args[0].strip())
	if ((n % 2) != 0):
	    global_list.append(0)
	else:
	    global_list.append((math.ceil((n / 4)) - 1))
	return global_list