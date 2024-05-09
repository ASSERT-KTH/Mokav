def patched_func(*args):
	global_list = []
	
	a = args[0].split(' ')
	b = args[1].split(' ')
	if ((((int(a[2]) - int(a[0])) % int(b[0])) != 0) or (((int(a[3]) - int(a[1])) % int(b[1])) != 0)):
	    global_list.append('NO')
	elif ((((int(a[2]) - int(a[0])) // int(b[0])) % 2) == (((int(a[3]) - int(a[1])) // int(b[1])) % 2)):
	    global_list.append('YES')
	else:
	    global_list.append('NO')
	return global_list