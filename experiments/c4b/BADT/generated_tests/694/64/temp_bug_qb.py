def original_func(*args):
	global_list = []
	
	x = args[0]
	if ((x == 'a1') or (x == 'a8') or (x == 'h1') or (x == 'h8')):
	    global_list.append(3)
	elif ((x.count('a') == 1) or ((x.count('h') == 1) and (x.count(('1' or '8')) == 0))):
	    global_list.append(5)
	elif ((x.count('1') == 1) or ((x.count('8') == 1) and (x.count('a') == 0) and x.count('h'))):
	    global_list.append(5)
	else:
	    global_list.append(8)
	return global_list