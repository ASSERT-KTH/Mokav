def patched_func(*args):
	global_list = []
	
	(a, b) = map(int, args[0].split())
	s = int((a ** 0.5))
	if ((s * (s + 1)) > b):
	    global_list.append('Valera')
	else:
	    global_list.append('Vladik')
	return global_list