def original_func(*args):
	global_list = []
	
	a = [int(i) for i in args[0].split()]
	p = int(a[0])
	n = int(a[1])
	if ((p == (n + 1)) or (p == n) or (n == (p + 1))):
	    global_list.append('YES')
	else:
	    global_list.append('NO')
	return global_list