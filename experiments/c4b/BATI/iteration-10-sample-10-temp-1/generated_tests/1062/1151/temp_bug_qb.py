def original_func(*args):
	global_list = []
	
	n = args[0]
	a = (n.count('4') + n.count('7'))
	if ((((a % 4) == 0) or ((a % 7) == 0)) and (a != 0)):
	    global_list.append('YES')
	else:
	    global_list.append('NO')
	return global_list