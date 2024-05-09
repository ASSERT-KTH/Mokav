def original_func(*args):
	global_list = []
	
	'input\n1 7 3\n'
	(a, b, c) = map(int, args[0].split())
	if (a == b):
	    global_list.append('YES')
	elif (c == 0):
	    global_list.append('NO')
	elif ((((b - a) % c) == 0) and (b > a) and (c > 0)):
	    global_list.append('YES')
	elif ((((b - a) % c) == 0) and (c < 0)):
	    global_list.append('YES')
	else:
	    global_list.append('NO')
	return global_list