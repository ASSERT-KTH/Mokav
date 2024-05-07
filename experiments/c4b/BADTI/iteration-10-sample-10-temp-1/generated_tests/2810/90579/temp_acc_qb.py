def patched_func(*args):
	global_list = []
	
	import sys
	n = int(args[0])
	if (n > 1):
	    if ((n % 2) == 0):
	        result = int(((n / 2) - 1))
	    else:
	        result = (int(((n / 2) - 1)) + 1)
	else:
	    result = 0
	global_list.append(result)
	return global_list