def patched_func(*args):
	global_list = []
	
	n = int(args[0])
	if (n == 1):
	    global_list.append('I hate it')
	else:
	    s = ''
	    for i in range((n - 1)):
	        if ((i % 2) == 0):
	            s += 'I hate that'
	        else:
	            s += 'I love that'
	        s += ' '
	    if (((n % 2) == 0) and (n != 1)):
	        s += 'I love it'
	    if (((n % 2) == 1) and (n != 1)):
	        s += 'I hate it'
	    global_list.append(s)
	return global_list