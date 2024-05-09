def original_func(*args):
	global_list = []
	
	k = int(args[0])
	r = 0
	for i in range((k - 1)):
	    r += ((k - i) * (i + 1))
	    if (i > 0):
	        r -= 1
	global_list.append((r + 1))
	return global_list