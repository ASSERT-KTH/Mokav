def original_func(*args):
	global_list = []
	
	a = int(args[0])
	b = ''
	for r in range(1, (a + 1)):
	    if ((r % 2) == 1):
	        b = (b + 'I hate that ')
	    else:
	        b = (b + 'I love that ')
	global_list.append(b)
	return global_list