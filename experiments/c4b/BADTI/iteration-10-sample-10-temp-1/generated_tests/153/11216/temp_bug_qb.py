def original_func(*args):
	global_list = []
	
	from math import ceil
	n = int(args[0])
	if ((n & 1) == 0):
	    ans = 0
	else:
	    ans = (ceil((n / 4)) - 1)
	global_list.append(ans)
	return global_list