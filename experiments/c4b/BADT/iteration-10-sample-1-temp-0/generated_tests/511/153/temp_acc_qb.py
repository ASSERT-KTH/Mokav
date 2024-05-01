def patched_func(*args):
	global_list = []
	
	(a, b, c) = map(int, args[0].split())
	k = (((a < b) * (c > 0)) + ((a > b) * (c < 0)))
	if (a == b):
	    global_list.append('YES')
	elif (c == 0):
	    global_list.append('NO')
	elif (((c == 0) and (a == b)) or (k and (((b - a) % c) == 0))):
	    global_list.append('YES')
	else:
	    global_list.append('NO')
	return global_list