def original_func(*args):
	global_list = []
	
	n = int(args[0])
	s1 = 'I hate it'
	s2 = 'I love it'
	s = ''
	for i in range(n):
	    if (s == ''):
	        s += s1
	    elif ((i % 2) == 0):
	        s += (' that ' + s1)
	    else:
	        s += (' that ' + s2)
	global_list.append(s)
	return global_list