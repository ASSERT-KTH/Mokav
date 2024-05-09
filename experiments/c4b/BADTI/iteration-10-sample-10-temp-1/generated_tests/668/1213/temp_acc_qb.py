def patched_func(*args):
	global_list = []
	
	n = int(args[0])
	s = ''
	for i in range(0, n):
	    if ((i % 2) == 0):
	        if (i != (n - 1)):
	            s = ((s + 'I hate that') + ' ')
	        else:
	            s = (s + 'I hate it')
	    elif (i != (n - 1)):
	        s = ((s + 'I love that') + ' ')
	    else:
	        s = (s + 'I love it')
	global_list.append(s)
	return global_list