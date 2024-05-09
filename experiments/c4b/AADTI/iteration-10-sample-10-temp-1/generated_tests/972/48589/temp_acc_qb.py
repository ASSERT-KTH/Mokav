def patched_func(*args):
	global_list = []
	
	(a, b) = map(int, args[0].split(' '))
	if (a == b == 0):
	    global_list.append('NO')
	elif ((abs((a - b)) == 1) or (a == b)):
	    global_list.append('YES')
	else:
	    global_list.append('NO')
	return global_list