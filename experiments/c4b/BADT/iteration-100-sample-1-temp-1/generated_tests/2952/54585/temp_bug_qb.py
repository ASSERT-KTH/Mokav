def original_func(*args):
	global_list = []
	
	(n, k) = list(map(int, args[0].split(' ')))
	if (((((n % k) % 2) == 0) or (((n % k) % 2) == 1)) and (n != k)):
	    global_list.append('NO')
	else:
	    global_list.append('YES')
	return global_list