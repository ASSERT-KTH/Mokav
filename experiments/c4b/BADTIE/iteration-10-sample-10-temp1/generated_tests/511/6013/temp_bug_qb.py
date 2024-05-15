def original_func(*args):
	global_list = []
	
	(a, b, c) = map(int, args[0].split(' '))
	if (c == 0):
	    if (a == b):
	        global_list.append('YES')
	    else:
	        global_list.append('NO')
	elif ((a + b) == 0):
	    if ((c % a) == 0):
	        global_list.append('YES')
	    else:
	        global_list.append('NO')
	elif ((abs((b - a)) % abs(c)) == 0):
	    global_list.append('YES')
	else:
	    global_list.append('NO')
	return global_list