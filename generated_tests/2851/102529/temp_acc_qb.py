def patched_func(*args):
	global_list = []
	
	ab = args[0]
	a = int(ab.split(' ')[0])
	b = int(ab.split(' ')[1])
	a1 = int((a ** (1 / 2)))
	b1 = int((((((4 * b) + 1) ** (1 / 2)) - 1) / 2))
	if ((a1 - b1) >= 1):
	    global_list.append('Valera')
	else:
	    global_list.append('Vladik')
	return global_list