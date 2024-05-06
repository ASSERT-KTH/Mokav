def original_func(*args):
	global_list = []
	
	n = int(args[0])
	a = ''
	if (n == 1):
	    global_list.append('I hate it')
	elif (n == 2):
	    global_list.append('I hate that I love it')
	else:
	    if ((n % 2) == 0):
	        for i in range(1, (n // 2)):
	            a = (a + 'I hate that I love that')
	        b = (a + ' I hate that I love it')
	    else:
	        for j in range(1, ((n // 2) + 1)):
	            a = (a + 'I hate that I love that')
	        b = (a + ' I hate it')
	    global_list.append(b)
	return global_list