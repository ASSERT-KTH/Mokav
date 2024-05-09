def original_func(*args):
	global_list = []
	
	(n, a, b) = map(str, args[0].split())
	n = int(n)
	if (b == 'week'):
	    if ((n == 5) or (n == 6)):
	        global_list.append(53)
	    else:
	        global_list.append(52)
	elif (n == 31):
	    global_list.append(7)
	elif ((n > 28) and (n <= 30)):
	    global_list.append(11)
	else:
	    global_list.append(12)
	return global_list