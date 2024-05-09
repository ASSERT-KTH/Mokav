def patched_func(*args):
	global_list = []
	
	import math
	(a, b) = map(int, args[0].split())
	for var in range(1, 1000):
	    if ((a * pow(3, var)) > (b * pow(2, var))):
	        global_list.append(var)
	        break
	return global_list