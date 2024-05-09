def patched_func(*args):
	global_list = []
	
	import math
	data = args[0].split()
	(N, X, Y) = (int(data[0]), int(data[1]), int(data[2]))
	clones = (math.ceil((N * (Y / 100))) - X)
	if (clones > 0):
	    global_list.append(clones)
	else:
	    global_list.append(0)
	return global_list