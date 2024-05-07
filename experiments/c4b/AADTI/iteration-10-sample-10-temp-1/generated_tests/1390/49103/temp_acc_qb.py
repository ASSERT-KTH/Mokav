def patched_func(*args):
	global_list = []
	
	import math
	n_x_y = list(map(int, args[0].split()))
	minn = math.ceil(((n_x_y[2] / 100) * n_x_y[0]))
	req = (minn - n_x_y[1])
	if (req < 0):
	    global_list.append('0')
	else:
	    global_list.append(req)
	return global_list