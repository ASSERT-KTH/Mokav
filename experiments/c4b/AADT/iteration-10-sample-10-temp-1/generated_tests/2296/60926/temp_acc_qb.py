def patched_func(*args):
	global_list = []
	
	lisa = args[0]
	index = 0
	for i in range(len(lisa)):
	    if (lisa[i] == ' '):
	        index = i
	global_list.append(int(((int(lisa[0:index]) * int(lisa[(index + 1):len(lisa)])) / 2)))
	return global_list