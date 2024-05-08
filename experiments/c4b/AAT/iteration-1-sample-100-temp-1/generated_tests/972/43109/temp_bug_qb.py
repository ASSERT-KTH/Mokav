def original_func(*args):
	global_list = []
	
	(a, b) = [int(x) for x in args[0].split()]
	if ((abs((a - b)) not in [0, 1]) or (a, (b == [0, 0]))):
	    global_list.append('NO')
	else:
	    global_list.append('YES')
	return global_list