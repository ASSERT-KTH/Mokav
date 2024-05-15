def patched_func(*args):
	global_list = []
	
	s = args[0]
	m = list(s)
	l = len(s)
	c = 0
	d = 0
	e = 0
	f = 0
	i = 0
	f = '1111111'
	g = '0000000'
	if (f in s):
	    global_list.append('YES')
	elif (g in s):
	    global_list.append('YES')
	else:
	    global_list.append('NO')
	return global_list