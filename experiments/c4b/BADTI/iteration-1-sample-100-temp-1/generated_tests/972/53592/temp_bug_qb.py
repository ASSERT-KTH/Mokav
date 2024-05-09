def original_func(*args):
	global_list = []
	
	R = (lambda : map(int, args[0].split()))
	(n, l) = R()
	if (((n - l) == 0) or ((n - l) == (- 1)) or ((n - l) == 1)):
	    global_list.append('YES')
	else:
	    global_list.append('NO')
	return global_list