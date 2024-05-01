def original_func(*args):
	global_list = []
	
	n = args[0]
	if (n.count('4') == len(n)):
	    global_list.append('YES')
	elif (n.count('7') == len(n)):
	    global_list.append('YES')
	elif ((n.count('4') + n.count('7')) == len(n)):
	    global_list.append('YES')
	else:
	    global_list.append('NO')
	return global_list