def patched_func(*args):
	global_list = []
	
	import math
	n = list(map(int, args[0].split()))
	k = (math.ceil(((n[0] * n[2]) / 100)) - n[1])
	if (k >= 0):
	    global_list.append(k)
	else:
	    global_list.append('0')
	return global_list