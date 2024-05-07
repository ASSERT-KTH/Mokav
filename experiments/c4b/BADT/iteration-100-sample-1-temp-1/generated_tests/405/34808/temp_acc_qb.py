def patched_func(*args):
	global_list = []
	
	s = oct(int(args[0]))
	counter = 0
	for c in s:
	    if (c == '1'):
	        counter += 1
	global_list.append(counter)
	return global_list