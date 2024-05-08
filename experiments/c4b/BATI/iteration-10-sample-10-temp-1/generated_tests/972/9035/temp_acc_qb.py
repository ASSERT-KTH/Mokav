def patched_func(*args):
	global_list = []
	
	a = [int(i) for i in args[0].split()]
	if (((a[0] - a[1]) >= (- 1)) and ((a[0] - a[1]) <= 1) and ((a[1] > 0) or (a[0] > 0))):
	    global_list.append('YES')
	else:
	    global_list.append('NO')
	return global_list