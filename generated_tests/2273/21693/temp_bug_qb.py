def original_func(*args):
	global_list = []
	
	T = args[0]
	t = int(T)
	a = 0
	i = 0
	while (a < t):
	    a = ((i * (i + 1)) / 2)
	    i = (i + 1)
	if (a == t):
	    global_list.append('yes')
	elif (t == 0):
	    global_list.append('NO')
	else:
	    global_list.append('NO')
	return global_list