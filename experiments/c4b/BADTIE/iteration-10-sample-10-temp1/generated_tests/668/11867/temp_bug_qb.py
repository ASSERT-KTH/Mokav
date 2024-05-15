def original_func(*args):
	global_list = []
	
	n = int(args[0])
	s = ''
	for i in range(1, n):
	    if ((i % 2) == 0):
	        s = (s + 'I love it')
	    else:
	        s = (s + 'I hate it')
	    s = (s + ' that ')
	if ((n % 2) == 0):
	    s = (s + 'I love it')
	else:
	    s = (s + 'I hate it')
	global_list.append(s)
	return global_list