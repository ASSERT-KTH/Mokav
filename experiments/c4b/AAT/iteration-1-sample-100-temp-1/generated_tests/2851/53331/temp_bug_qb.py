def original_func(*args):
	global_list = []
	
	(a, b) = list(map(int, args[0].split()))
	d1 = (a ** 0.5)
	d2 = (b ** 0.5)
	if (d1 > d2):
	    global_list.append('Vladik')
	else:
	    global_list.append('Valera')
	return global_list