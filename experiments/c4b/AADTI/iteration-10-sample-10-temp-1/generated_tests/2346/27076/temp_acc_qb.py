def patched_func(*args):
	global_list = []
	
	(a, b, c, d) = sorted(map(int, args[0].split()))
	if ((d < (c + b)) or (c < (b + a))):
	    global_list.append('TRIANGLE')
	elif ((d == (c + b)) or (c == (b + a))):
	    global_list.append('SEGMENT')
	else:
	    global_list.append('IMPOSSIBLE')
	return global_list