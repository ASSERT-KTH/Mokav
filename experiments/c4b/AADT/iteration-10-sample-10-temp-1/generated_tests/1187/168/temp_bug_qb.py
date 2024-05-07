def original_func(*args):
	global_list = []
	
	n = args[0][:11]
	a = n[0]
	b = a.upper()
	c = n[1:]
	d = c.lower()
	global_list.append((b + d))
	return global_list