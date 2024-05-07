def patched_func(*args):
	global_list = []
	
	n = int(args[0])
	for i in range((n + 1), 10000):
	    if (len(set(str(i))) == len(str(i))):
	        global_list.append(i)
	        break
	return global_list