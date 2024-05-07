def patched_func(*args):
	global_list = []
	
	from math import ceil
	n = int(args[0])
	if (n < 6):
	    global_list.append(0)
	elif (n % 2):
	    global_list.append(0)
	else:
	    x = (n // 2)
	    global_list.append((ceil((x / 2)) - 1))
	return global_list