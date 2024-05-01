def original_func(*args):
	global_list = []
	
	n = int(args[0])
	s = ''
	s += 'I hate it'
	for i in range(1, n):
	    s += ' '
	    if ((i % 2) == 0):
	        s += 'I hate it'
	    else:
	        s += 'I love it'
	global_list.append(s)
	return global_list