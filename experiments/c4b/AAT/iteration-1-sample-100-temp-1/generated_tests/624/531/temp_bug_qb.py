def original_func(*args):
	global_list = []
	
	'input\n3 10 4\n'
	(t, s, x) = map(int, args[0].split())
	if (((((x - t) % s) == 0) or ((((x - t) - 1) % s) == 0)) and ((x - t) != 1)):
	    global_list.append('YES')
	else:
	    global_list.append('NO')
	return global_list