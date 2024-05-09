def original_func(*args):
	global_list = []
	
	(a, b, c, d) = sorted(map(int, args[0].split()))
	global_list.append(a, b, c, d)
	if ((d < (c + b)) or (c < (b + a))):
	    global_list.append('TRIANGLE')
	elif ((d == (c + b)) or (c == (b + a))):
	    global_list.append('SEGMENT')
	else:
	    global_list.append('IMPOSSIBLE')
	return global_list