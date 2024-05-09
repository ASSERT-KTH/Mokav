def patched_func(*args):
	global_list = []
	
	T = args[0]
	t = int(T)
	a = 0
	i = 0
	while (a < t):
	    a = ((i * (i + 1)) / 2)
	    i = (i + 1)
	if (t == 0):
	    global_list.append('NO')
	elif (a == t):
	    global_list.append('YES')
	else:
	    global_list.append('NO')
	return global_list