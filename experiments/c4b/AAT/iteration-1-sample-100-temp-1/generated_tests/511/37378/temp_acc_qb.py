def patched_func(*args):
	global_list = []
	
	(a, b, c) = map(int, args[0].split(' '))
	if (((a != b) and (c == 0)) or ((b > a) and (c < 0))):
	    global_list.append('NO')
	elif ((a == b) or ((b > a) and (c > 0) and (((b - a) % c) == 0)) or ((a > b) and (c < 0) and (((a - b) % c) == 0))):
	    global_list.append('YES')
	else:
	    global_list.append('NO')
	return global_list