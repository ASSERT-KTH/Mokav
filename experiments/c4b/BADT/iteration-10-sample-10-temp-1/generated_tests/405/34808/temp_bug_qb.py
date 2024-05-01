def original_func(*args):
	global_list = []
	
	s = args[0]
	counter = 0
	for c in s:
	    if (c == '1'):
	        counter += 1
	global_list.append(oct(counter)[2:])
	return global_list