def patched_func(*args):
	global_list = []
	
	times = int(args[0])
	ane = list(args[1])
	count = 0
	for i in range((len(ane) - 1)):
	    if (ane[i] == ane[(i + 1)]):
	        count = (count + 1)
	global_list.append(count)
	return global_list