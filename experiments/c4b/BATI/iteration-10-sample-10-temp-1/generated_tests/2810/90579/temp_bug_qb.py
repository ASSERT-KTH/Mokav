def original_func(*args):
	global_list = []
	
	import sys
	n = int(args[0])
	if ((n % 2) == 0):
	    result = int(((n / 2) - 1))
	else:
	    result = (int(((n / 2) - 1)) + 1)
	global_list.append(result)
	return global_list