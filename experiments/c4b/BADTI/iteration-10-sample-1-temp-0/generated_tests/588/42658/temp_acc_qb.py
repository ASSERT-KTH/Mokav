def patched_func(*args):
	global_list = []
	
	import math
	N = int(args[0].split()[0])
	if (N % 2):
	    global_list.append(int(((N - 1) / 2)))
	else:
	    global_list.append(int(((N - pow(2, int(math.log2(N)))) / 2)))
	return global_list