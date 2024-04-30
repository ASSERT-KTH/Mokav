def original_func(*args):
	global_list = []
	
	a = int(args[0])
	b = a
	str = ''
	while (b > 0):
	    if (((a - b) % 2) == 0):
	        str += 'I hate it '
	        b -= 1
	    else:
	        str += 'I love it '
	        b -= 1
	global_list.append(str)
	return global_list