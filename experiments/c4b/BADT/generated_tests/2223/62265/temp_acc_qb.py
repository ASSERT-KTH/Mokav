def patched_func(*args):
	global_list = []
	
	import sys
	watermelon = int(args[0])
	if (((watermelon % 2) == 0) and (watermelon > 2)):
	    global_list.append('YES')
	else:
	    global_list.append('NO')
	return global_list