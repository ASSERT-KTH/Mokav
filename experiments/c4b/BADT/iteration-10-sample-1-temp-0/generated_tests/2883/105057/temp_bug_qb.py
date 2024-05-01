def original_func(*args):
	global_list = []
	
	a = args[0].split(' ')
	b = args[1].split(' ')
	if (((int(a[2]) % int(b[0])) == 0) and ((int(a[3]) % int(b[1])) == 0)):
	    global_list.append('YES')
	else:
	    global_list.append('NO')
	return global_list