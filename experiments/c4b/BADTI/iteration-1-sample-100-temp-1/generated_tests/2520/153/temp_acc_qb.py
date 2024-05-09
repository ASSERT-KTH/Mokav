def patched_func(*args):
	global_list = []
	
	(n, m) = map(int, args[0].split())
	x = str(max(n, m))
	if (x == '1'):
	    global_list.append('1/1')
	elif (x == '2'):
	    global_list.append('5/6')
	elif (x == '3'):
	    global_list.append('2/3')
	elif (x == '4'):
	    global_list.append('1/2')
	elif (x == '5'):
	    global_list.append('1/3')
	else:
	    global_list.append('1/6')
	return global_list