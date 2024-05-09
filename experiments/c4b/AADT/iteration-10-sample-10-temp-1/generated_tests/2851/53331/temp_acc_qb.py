def patched_func(*args):
	global_list = []
	
	(a, b) = list(map(int, args[0].split()))
	d1 = int((a ** 0.5))
	d2 = int(((((1 + (4 * b)) ** 0.5) - 1) / 2))
	if (d1 > d2):
	    global_list.append('Valera')
	else:
	    global_list.append('Vladik')
	return global_list