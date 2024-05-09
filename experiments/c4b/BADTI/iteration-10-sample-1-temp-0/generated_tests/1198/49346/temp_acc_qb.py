def patched_func(*args):
	global_list = []
	
	x = args[0]
	a = list()
	for i in range(0, len(x)):
	    a.append(x[i])
	if (('H' == x[0]) or ('Q' == x[0]) or ('9' == x[0]) or ('H' in a) or ('Q' in a) or ('9' in a)):
	    global_list.append('YES')
	else:
	    global_list.append('NO')
	return global_list