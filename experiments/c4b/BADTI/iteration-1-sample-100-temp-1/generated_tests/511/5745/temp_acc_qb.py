def patched_func(*args):
	global_list = []
	
	(a, b, c) = map(int, args[0].split(' '))
	if (c == 0):
	    if (b == a):
	        global_list.append('YES')
	    else:
	        global_list.append('NO')
	elif ((((b - a) % c) == 0) and (((c > 0) and (a <= b)) or ((c < 0) and (a >= b)))):
	    global_list.append('YES')
	else:
	    global_list.append('NO')
	return global_list